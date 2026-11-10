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

# TP – Optimisation Docker

## 1. Objectif du TP

L'objectif de ce TP est de comprendre le fonctionnement de Docker et d'apprendre à optimiser une image Docker afin de réduire sa taille, faciliter son déploiement et améliorer sa maintenance.

L'application utilisée est une application Node.js basée sur Express et MongoDB.

## 2. Optimisations réalisées

### Étape 1 – Image initiale (Baseline)

L'image initiale utilisait `node:latest`.

- Taille disque : 1,88 GB
- Taille du contenu : 474 MB

Cette version sert de référence pour comparer les optimisations.

### Étape 2 – Organisation du Dockerfile

Les instructions `COPY package*.json ./` et `RUN npm install` ont été placées avant `COPY . .` afin de favoriser la réutilisation du cache Docker.

Un fichier `.dockerignore` a également été créé pour exclure :
- `node_modules`
- `.git`
- `npm-debug.log`

Résultat : cette première version n'a pas réduit la taille de l'image.

### Étape 3 – Utilisation de node:22-slim

L'image de base a été remplacée par `node:22-slim`.

Cette version utilise une image Node.js plus légère que l'image initiale.

### Étape 4 – Utilisation de npm ci

La commande `npm install` a été remplacée par `npm ci`, qui s'appuie sur le fichier `package-lock.json`.

Le script `npm run build` a été supprimé, car il ne réalisait aucune compilation : il affichait simplement un message.

Résultat :
- Taille disque : 358 MB
- Taille du contenu : 86 MB

### Étape 5 – Utilisation de node:22-alpine

L'image de base a été remplacée par `node:22-alpine`, une distribution Linux légère.

Résultat :
- Taille disque : 271 MB
- Taille du contenu : 67,5 MB

### Étape 6 – Multi-stage build

Un Dockerfile multi-stage a été mis en place avec deux étapes :
- Une première étape pour installer les dépendances.
- Une deuxième étape pour créer l'image finale avec uniquement les dépendances de production et les fichiers nécessaires à l'exécution.

La commande `npm ci --omit=dev` permet d'exclure les dépendances de développement, notamment `nodemon`.

Résultat :
- Taille disque : 266 MB
- Taille du contenu : 66,6 MB

## 3. Tableau comparatif

| Version | Taille disque | Taille du contenu |
|---|---:|---:|
| Baseline | 1,88 GB | 474 MB |
| Optimisation 1 | 1,89 GB | 476 MB |
| Optimisation 2 | 1,89 GB | 476 MB |
| Optimisation 3 | 358 MB | 86 MB |
| Optimisation 4 | 271 MB | 67,5 MB |
| Optimisation 5 | 266 MB | 66,6 MB |

## 4. Résultat final

La taille du contenu de l'image est passée de 474 MB à 66,6 MB, soit une réduction d'environ 85,9 %.

L'application a été testée avec les différentes versions et fonctionne correctement.

## 5. Conclusion

Ce TP m'a permis de découvrir plusieurs bonnes pratiques pour optimiser les images Docker : utiliser un fichier `.dockerignore`, organiser les instructions pour profiter du cache, choisir une image de base légère et utiliser un multi-stage build.

Les mesures montrent que le choix de l'image de base et la réduction des dépendances présentes dans l'image finale ont contribué à diminuer fortement sa taille.