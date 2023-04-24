WHS Project: OULFA OUAHOUDA

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wjmO5Bst)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10854119&assignment_repo_type=AssignmentRepo)

## Comment lancer le backend ?
go to whs_backend and start the big sh file called start.sh

or 

sudo -E /home/pc/github-classroom/esisa-dev/webhomespace-OulfaOuahouda2023/whs_backend/venv/bin/python3 app.py 

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


## Feuille de route

1. Installation des outils nécessaires : Pour travailler avec Angular, il faut installer le CLI d'Angular, qui permet de générer des projets, des composants, des services et bien plus encore.

2. Génération d'un projet Angular : Utilisez le CLI d'Angular pour générer un nouveau projet en exécutant la commande `ng new <nom-du-projet>`. Cela va créer une nouvelle application Angular avec une structure de fichiers de base.

3. Création des composants : Créez les composants nécessaires pour votre application (par exemple, un composant pour la page de connexion, un pour la page d'accueil, un pour la page de recherche, etc.). Vous pouvez utiliser le CLI d'Angular pour générer automatiquement ces composants en exécutant la commande `ng generate component <nom-du-composant>`.

4. Mise en place de l'authentification : Créez un formulaire de connexion et utilisez le service de connexion Flask pour vérifier les informations d'identification de l'utilisateur. Si les informations d'identification sont correctes, stockez un jeton d'authentification dans la session pour authentifier les demandes ultérieures.

5. Affichage des fichiers et dossiers : Créez une page d'accueil pour afficher les fichiers et dossiers de l'utilisateur actuellement connecté. Utilisez le service Flask pour récupérer les données du répertoire et les afficher dans un tableau.

6. Mise en place de la recherche : Créez une page de recherche qui permet à l'utilisateur de rechercher des fichiers par nom ou extension. Utilisez le service Flask pour effectuer la recherche et afficher les résultats dans un tableau.

7. Téléchargement du répertoire : Ajoutez un bouton de téléchargement sur la page d'accueil qui permet à l'utilisateur de télécharger le répertoire complet au format zip. Utilisez le service Flask pour créer le fichier zip et le renvoyer à l'utilisateur.

8. Mise en place de la déconnexion : Ajoutez un bouton de déconnexion sur la page d'accueil qui permet à l'utilisateur de se déconnecter de l'application. Utilisez le service Flask pour supprimer le jeton d'authentification et rediriger l'utilisateur vers la page de connexion.

9. Déploiement de l'application : Déployez l'application en tant que service Linux pour permettre aux utilisateurs d'y accéder via un navigateur Web.


Étapes pour créer les composants et consommer l'API Flask
Générer un nouveau projet Angular en exécutant la commande ng new <nom-du-projet> --routing. Cela va créer une nouvelle application Angular avec une structure de fichiers de base, incluant un fichier app-routing.module.ts pour gérer les routes de l'application.

Créer les services nécessaires pour communiquer avec l'API Flask en exécutant la commande ng generate service <nom-du-service>. Les services sont des classes qui permettent de récupérer des données depuis une source externe (comme une API) et de les manipuler dans l'application.

Créer les composants nécessaires pour votre application en exécutant la commande ng generate component <nom-du-composant>. Les composants sont des éléments d'interface utilisateur réutilisables qui permettent de structurer l'application en sous-sections.

Dans le fichier app.module.ts, importer les modules nécessaires pour votre application (par exemple, HttpClientModule pour communiquer avec l'API Flask via HTTP).

Dans le fichier de service, écrire le code pour communiquer avec l'API Flask (par exemple, en utilisant la fonction HttpClient pour envoyer des requêtes HTTP GET/POST).

Dans le fichier de composant, importer le service correspondant et appeler les fonctions nécessaires pour récupérer les données depuis l'API Flask.

Utiliser les données récupérées pour afficher les informations souhaitées dans le composant en utilisant les directives d'Angular (comme *ngFor pour afficher une liste de résultats).

Utiliser le fichier app-routing.module.ts pour définir les routes de l'application et naviguer entre les différents composants.

