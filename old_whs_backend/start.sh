#!/bin/bash

# Active l'environnement virtuel
source venv/bin/activate

# Définit les variables d'environnement pour Flask
export FLASK_APP=app.py
export FLASK_ENV=development

# Démarre le serveur Flask
flask run --port 5001




