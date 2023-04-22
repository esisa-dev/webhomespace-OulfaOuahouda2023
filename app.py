from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, make_response
import os
import zipfile
import io
from utils.auth import authenticate
from utils.file_management import get_directory_data, search_files, read_file_content

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if authenticate(username, password):
            response = make_response(redirect(url_for('home')))
            response.set_cookie('username', username)
            return response
        else:
            flash('Invalid credentials', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    path = request.args.get('path', f'/home/{username}')
    dirs, files = get_directory_data(path, username)
    return render_template('home.html', dirs=dirs, files=files, path=path, username=username)

@app.route('/file_content', methods=['GET'])
def file_content():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    file_path = request.args.get('path')
    content = read_file_content(file_path, username)
    return content

@app.route('/search', methods=['GET'])
def search():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    query = request.args.get('query')
    path = f'/home/{username}'
    results = search_files(query, path, username)
    return render_template('search.html', results=results, path=path, username=username)

@app.route('/download', methods=['GET'])
def download():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    path = f'/home/{username}'
    zip_filename = f'{username}_home.zip'
    data = io.BytesIO()
    with zipfile.ZipFile(data, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                zf.write(full_path, full_path.replace(path, '', 1))
    data.seek(0)
    response = send_from_directory(directory=data, filename=zip_filename, as_attachment=True)
    response.headers['Content-Disposition'] = f'attachment; filename={zip_filename}'
    return response

@app.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)