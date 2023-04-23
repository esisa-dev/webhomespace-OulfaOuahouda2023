WHS Project: OULFA OUAHOUDA
PLEASE SEE BACKEND IN WHS_BACKEND
PLEASE SEE FRONT END IN WHS_FRONTEND

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wjmO5Bst)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10854119&assignment_repo_type=AssignmentRepo)


## Endpoints API Flask

### `POST /login`
- Description : Connecte un utilisateur en utilisant les informations d'identification spécifiées.
- Request body : `{ "username": "nom d'utilisateur", "password": "mot de passe" }`
- Responses :
    - `200 OK` : si l'utilisateur a été connecté avec succès.
    - `401 Unauthorized` : si les informations d'identification sont incorrectes.
    - `400 Bad Request` : si les données de demande sont invalides.

### `POST /logout`
- Description : Déconnecte l'utilisateur actuellement connecté.
- Responses :
    - `200 OK` : si l'utilisateur a été déconnecté avec succès.

### `GET /home`
- Description : Affiche la page d'accueil de l'utilisateur actuellement connecté.
- Query parameters :
    - `path` (optionnel) : spécifie le chemin du répertoire à afficher.
- Responses :
    - `200 OK` : renvoie la page d'accueil avec les fichiers et dossiers de l'utilisateur.

### `GET /file_content`
- Description : Récupère le contenu d'un fichier.
- Query parameters :
    - `path` : spécifie le chemin du fichier.
- Responses :
    - `200 OK` : renvoie le contenu du fichier.

### `GET /search`
- Description : Recherche des fichiers dans le répertoire de l'utilisateur actuellement connecté.
- Query parameters :
    - `query` : spécifie la chaîne de caractères à rechercher dans les noms de fichier.
- Responses :
    - `200 OK` : renvoie la liste des fichiers correspondants à la recherche.

### `GET /download`
- Description : Télécharge le répertoire de l'utilisateur actuellement connecté au format zip.
- Responses :
    - `200 OK` : renvoie le fichier zip à télécharger.
