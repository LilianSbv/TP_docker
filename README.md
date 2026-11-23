# TP Docker

# Partie 1 : Manipulation de base de Docker

Dans cette première partie, j'ai découvert les principales commandes Docker permettant de manipuler les images et les conteneurs.

J'ai notamment utilisé les commandes suivantes :

- `docker --version` pour vérifier l'installation.
- `docker images` pour afficher les images disponibles.
- `docker pull hello-world` pour récupérer une image.
- `docker run hello-world` pour lancer un conteneur.
- `docker ps` et `docker ps -a` pour consulter les conteneurs.

Ces manipulations m'ont permis de comprendre le fonctionnement de base de Docker et la différence entre une image et un conteneur.

---

# Partie 2 : Serveur web Nginx

J'ai utilisé l'image officielle Nginx afin de lancer un serveur web dans un conteneur Docker.

Le conteneur a été lancé avec le port 8080 de ma machine relié au port 80 du conteneur, ce qui permet d'accéder à la page Nginx depuis le navigateur à l'adresse :

http://localhost:8080

Cette partie m'a permis de comprendre comment rendre un service exécuté dans un conteneur accessible depuis ma machine.

---

# Partie 3 : Application Flask

## Objectif

J'ai créé une application web simple avec Flask et je l'ai exécutée dans un conteneur Docker.

Les fichiers utilisés sont `app.py`, `requirements.txt` et `Dockerfile`.

## Dockerfile

J'ai utilisé une image `python:3.11-slim` pour construire l'application.

Le Dockerfile permet d'installer les dépendances, de copier les fichiers nécessaires et de lancer l'application sur le port 5000.

J'ai choisi une image slim afin de limiter la taille de l'image Docker.

## Lancement de l'application

L'image est construite avec :

```bash
docker build -t flask-app .
```

Puis le conteneur est lancé avec :

```bash
docker run -d -p 5000:5000 --name flask-container flask-app
```

L'application est accessible à l'adresse :

http://localhost:5000

---

# Partie 4 : Docker Compose et MongoDB

## Objectif

J'ai ensuite modifié mon application Flask afin de pouvoir la connecter à une base de données MongoDB.

Pour cela, j'ai utilisé Docker Compose afin de gérer les deux services :

- Flask pour l'application web.
- MongoDB pour la base de données.

## Configuration

Le fichier `docker-compose.yml` permet de lancer les deux services ensemble.

J'ai également mis en place :

- Des variables d'environnement pour la connexion à MongoDB.
- Un volume pour conserver les données de la base.
- Un healthcheck pour vérifier que MongoDB est opérationnel.
- Une dépendance entre Flask et MongoDB afin que Flask attende que la base de données soit prête.

## Vérification

Les deux services sont lancés avec :

```bash
docker compose up --build -d
```

L'application Flask est accessible à l'adresse :

http://localhost:5000

J'ai également ajouté une route `/db-check` permettant de vérifier la connexion à MongoDB :

http://localhost:5000/db-check

Cette route permet de vérifier que l'application arrive bien à communiquer avec la base de données.

---

# Partie 5 : Optimisation Docker d'une application Node.js

## Objectif

L'objectif de cette partie était d'optimiser progressivement le Dockerfile d'une application Node.js afin de réduire la taille de l'image et d'améliorer sa configuration.

## Optimisations réalisées

J'ai réalisé plusieurs modifications au cours des différentes étapes :

- Réorganisation des instructions du Dockerfile pour améliorer l'utilisation du cache.
- Mise en place d'un fichier `.dockerignore` afin d'exclure les fichiers inutiles.
- Remplacement de l'image initiale `node:latest` par `node:22-slim`.
- Utilisation de `npm ci` pour installer les dépendances.
- Passage à `node:22-alpine` pour réduire davantage la taille de l'image.
- Mise en place d'un multi-stage build.
- Suppression des dépendances de développement dans l'image finale.
- Utilisation de `NODE_ENV=production`.
- Utilisation de l'utilisateur non-root `node`.

## Comparaison des tailles

| Étape | Taille disque | Taille du contenu |
|---|---:|---:|
| Version initiale | 1,88 GB | 474 MB |
| Organisation du Dockerfile | 1,89 GB | 476 MB |
| Optimisation intermédiaire | 1,89 GB | 476 MB |
| `node:22-slim` | 358 MB | 86 MB |
| `node:22-alpine` | 271 MB | 67,5 MB |
| Multi-stage build | 266 MB | 66,6 MB |

La taille du contenu est passée de 474 MB à 66,6 MB.

Les optimisations les plus importantes ont été le choix d'une image de base plus légère et la réduction des dépendances présentes dans l'image finale.

---
