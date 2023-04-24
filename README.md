WHS Project: OULFA OUAHOUDA

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wjmO5Bst)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10854119&assignment_repo_type=AssignmentRepo)

# Comment lancer le backend ?
go to whs_backend and start the big sh file called start.sh
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python3 app.py

or 

sudo -E /home/pc/github-classroom/esisa-dev/webhomespace-OulfaOuahouda2023/whs_backend/venv/bin/python3 app.py 

# WHS Web Home Services : Endpoints API Flask
- / : Affichage de la page d'accueil.

-/browse : Affichage des fichiers et des dossiers de l'espace utilisateur.

-/browse/<path:subpath> : Affichage des fichiers et des dossiers dans le sous-dossier spécifié.

-/login : Page de connexion pour l'utilisateur.

-/logout : Déconnexion de l'utilisateur.

-/search : Recherche de fichiers et de dossiers dans l'espace utilisateur.

-/upload : Téléchargement de fichiers sur l'espace utilisateur.

-/download/<path:subpath>/<string:filename> : Téléchargement d'un fichier spécifié.

-/download-as-file/<path:subpath>/<string:filename> : Téléchargement d'un fichier spécifié en utilisant le nom de fichier original.

-/delete/<path:subpath>/<string:filename> : Suppression d'un fichier spécifié.

-/delete-dir/<path:subpath>/<string:dirname> : Suppression d'un dossier spécifié.

-/create-dir/<path:subpath>/<string:dirname> : Création d'un nouveau dossier dans le sous-dossier spécifié.
