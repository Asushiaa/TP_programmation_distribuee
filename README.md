
L'application permet de consulter les chats d'un refuge, d'afficher leurs informations et de modifier leur statut (disponible ou adopté).

## Lancer l'application avec Docker

L'image est disponible sur Docker Hub : [dinakerk/cats-service](https://hub.docker.com/r/dinakerk/cats-service)

Pour la récupérer :

```bash
docker pull dinakerk/cats-service:latest
```

Pour lancer l'application :

```bash
docker run -p 5000:5000 dinakerk/cats-service:latest
```

L'API est ensuite accessible à l'adresse [http://localhost:5000/cats](http://localhost:5000/cats).

## Technologies utilisées

Python, Flask, Docker.
