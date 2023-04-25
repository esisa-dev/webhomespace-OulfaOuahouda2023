from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, send_file
from flask_bootstrap import Bootstrap
from flask import send_from_directory
import os
import logging
import spwd
import pwd
import grp
import hashlib
import binascii
from pathlib import Path
import pam

app = Flask(__name__)
app.secret_key = os.urandom(24)
Bootstrap(app)
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def index():
    if 'username' in session:
        num_files = len(list_files(Path.home())[1])
        return render_template('index.html', num_files=num_files)
    return render_template('index.html')

@app.route('/browse/<path:subpath>')
def browse_subpath(subpath):
    if 'username' not in session:
        return redirect(url_for('index'))

    base_path = Path.home()
    target_path = base_path / subpath

    if not target_path.exists() or not target_path.is_dir():
        flash("Le chemin spécifié n'existe pas ou n'est pas un répertoire.")
        return redirect(url_for('browse'))

    dirs, files = list_files(target_path)
    return render_template('browse.html', dirs=dirs, files=files, subpath=subpath)


@app.route('/download/<path:subpath>/<string:filename>')
def download_file(subpath, filename):
    if 'username' not in session:
        return redirect(url_for('index'))

    base_path = Path.home()
    target_path = base_path / subpath

    if not target_path.exists() or not target_path.is_dir():
        flash("Le chemin spécifié n'existe pas ou n'est pas un répertoire.")
        return redirect(url_for('browse'))

    return send_from_directory(directory=target_path, filename=filename)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        user = pwd.getpwnam(username)
    except KeyError:
        flash("Nom d'utilisateur ou mot de passe incorrect.")
        return redirect(url_for('index'))

    if authenticate(username, password):
        session['username'] = username
        session['uid'] = user.pw_uid
        session['gid'] = user.pw_gid
        logging.info(f"{username} s'est connecté")
        return redirect(url_for('browse'))
    else:
        flash("Nom d'utilisateur ou mot de passe incorrect.")
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if 'username' in session:
        logging.info(f"{session['username']} s'est déconnecté")
        session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/browse', defaults={'subpath': ''})
@app.route('/browse/<path:subpath>')
def browse(subpath):
    if 'username' not in session:
        return redirect(url_for('login'))

    base_dir = get_base_dir(session['username'])
    current_dir = os.path.join(base_dir, subpath)

    if not os.path.exists(current_dir) or not os.path.isdir(current_dir):
        return "Dossier introuvable.", 404

    dirs, files = get_dirs_and_files(current_dir)
    num_files = len(files)
    num_dirs = len(dirs)
    space = human_readable_size(os.statvfs(base_dir).f_frsize * os.statvfs(base_dir).f_bavail)

    return render_template('browse.html', dirs=dirs, files=files, subpath=subpath, num_files=num_files, num_dirs=num_dirs, space=space)


def human_readable_size(size, decimal_places=1):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"



def get_base_dir(username):
    base_dir = os.path.join("/home", username)
    return base_dir


def get_dirs_and_files(path):
    dirs = []
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)
            elif entry.is_dir():
                dirs.append(entry.name)

    return dirs, files

@app.route('/search', methods=['POST'])
def search():
    if 'username' not in session:
        return redirect(url_for('index'))

    base_path = Path.home()
    query = request.form['query']
    dirs, files = search_files(base_path, query)
    return render_template('browse.html', dirs=dirs, files=files)

def verify_password(stored_password, provided_password):
    salt, stored_hash = stored_password.split('$')[3:5]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), binascii.unhexlify(salt), 5000)
    return stored_hash == binascii.hexlify(pwdhash).decode('utf-8')

def list_files(path):
    dirs = []
    files = []
    for item in os.listdir(path):
        item_path = path / item
        if os.path.isdir(item_path):
            dirs.append(str(item_path))
        else:
            files.append(str(item_path))
    return dirs, files


def search_files(path, query):
    dirs = []
    files = []
    for item in os.listdir(path):
        item_path = path / item
        if os.path.isdir(item_path):
            if query.lower() in item.lower():
                dirs.append(item)
            subdirs, subfiles = search_files(item_path, query)
            dirs.extend(subdirs)
            files.extend(subfiles)
        elif query.lower() in item.lower():
            files.append(item)
    return dirs, files

@app.route('/download/<path:filepath>')
def download(filepath):
    if 'username' not in session:
        return redirect(url_for('index'))

    base_path = Path.home()
    full_path = base_path / filepath

    if os.path.isfile(full_path):
        logging.info(f"{session['username']} a téléchargé le fichier {filepath}")
        return send_from_directory(directory=base_path, filename=filepath, as_attachment=True)

    flash("Fichier introuvable.")
    return redirect(url_for('browse'))

def authenticate(username, password):
    auth = pam.pam()
    return auth.authenticate(username, password)

def generate_download_url(filepath):
    return url_for('download_as_file', filepath=filepath)

def generate_download_url_rel(filepath):
    # Retirer "/home/pc" du chemin absolu
    rel_path = str(Path(filepath).relative_to(Path.home()))
    return url_for('download_as_file', filepath=rel_path)


@app.route('/download-as-file/<path:filepath>')
def download_as_file(filepath):
    if 'username' not in session:
        return redirect(url_for('index'))
    
    base_path = str(Path.home() / session['username'])
    full_path = os.path.join(base_path, filepath[1:])  # Supprimer la barre oblique initiale
    filename = os.path.basename(full_path)
    return send_file(full_path, as_attachment=True, attachment_filename=filename)

@app.route('/download-as-file/<path:subpath>/<string:filename>')
def download_file_as_file(subpath, filename):
    if 'username' not in session:
        return redirect(url_for('index'))

    base_path = Path.home()
    target_path = base_path / subpath

    if not target_path.exists() or not target_path.is_dir():
        flash("Le chemin spécifié n'existe pas ou n'est pas un répertoire.")
        return redirect(url_for('browse'))

    # Ajouter cette ligne pour obtenir le chemin complet du fichier
    file_path = target_path / filename

    if not file_path.exists() or not file_path.is_file():
        flash("Le fichier spécifié n'existe pas ou n'est pas un fichier.")
        return redirect(url_for('browse'))

    logging.info(f"{session['username']} a téléchargé le fichier {filename}")
    return send_file(file_path, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True, port=5056)