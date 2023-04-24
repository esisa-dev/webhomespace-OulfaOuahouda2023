import os
'''
Oulfa please make doc from this -Islam 
get_directory_data: récupère les données du répertoire spécifié (répertoires et fichiers) en utilisant os.scandir.
search_files: recherche des fichiers qui contiennent la chaîne de caractères query dans leur nom en utilisant os.walk.
read_file_content: lit le contenu du fichier spécifié en utilisant la fonction open.
get_file_size: récupère la taille du fichier spécifié en utilisant os.path.getsize.
'''


def get_directory_data(path, username):
    dirs = []
    files = []
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                dirs.append({"name": entry.name, "path": entry.path})
            elif entry.is_file():
                files.append({"name": entry.name, "path": entry.path})
    return dirs, files


def search_files(query, path, username):
    results = []

    for root, _, files in os.walk(path):
        for file in files:
            if query in file:
                file_path = os.path.join(root, file)
                results.append(file_path)

    return results

def read_file_content(file_path, username):
    try:
        with open(file_path, "r") as file:
            content = file.read()
    except IOError:
        content = "Error reading the file"

    return content

def get_file_size(path, username):
    try:
        file_size = os.path.getsize(path)
    except OSError:
        file_size = 0

    return file_size
