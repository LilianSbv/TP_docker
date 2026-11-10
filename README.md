# TP Docker – Application Flask

## 1. Présentation du projet

Ce projet consiste à créer une application web avec Flask et à la conteneuriser avec Docker.

## 2. Structure du projet

```text
TP_docker/
├── .gitignore
├── README.md
└── Exercice/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

## 3. Technologies utilisées

- Python
- Flask
- Docker
- Git et GitHub

## 4. Construire l'image Docker

Depuis le dossier `Exercice`, exécuter :

```bash
docker build -t flask-app .
```

## 5. Lancer le conteneur

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

## 6. Tester l'application

Ouvrir un navigateur à l'adresse :

http://localhost:5000

L'application affiche un message de bienvenue.

## 7. Arrêter le conteneur

```bash
docker stop flask-container
docker rm flask-container
```

## 8. Gestion du code avec Git

Le projet est versionné avec Git et hébergé sur GitHub.

Pour envoyer les modifications :

```bash
git add .
git commit -m "Ajout du README"
git push
```