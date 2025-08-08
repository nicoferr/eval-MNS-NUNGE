# Read-me

<center>Vous pouvez modifier ce fichier (cf. Brief)</center>

## Comment gérer cette évaluation ?

1. Le rendu s'effectuera **uniquement** au travers de Github Classroom (clonez bien le repository créé par Github Classroom, et travaillez dedans. N'en recréez pas un nouveau). 
2. Une Pull-Request est automatiquement générée par Github Classroom, **ne la fermez pas**. Elle me permettra de vous faire un feedback sous forme de code annoté. 
3. Mettez-vous en condition d'une mise en situation professionnelle : le client (fictif, bien entendu) attend une app fonctionnelle qui répond au besoin énoncé, c'est tout :) 
4. Lisez bien l'entièreté du brief avant de démarrer, n'hésitez pas à poser votre architecture sur papier (ou du moins à y réfléchir sur un support autre que l'IDE) avant de coder. 

➡️ [Cliquez ici pour lire le brief du client](BRIEF.md)

## Choix du framework et du modèle IA

### Framework python

Le projet est développé à l'aide de Flask car l'application est petite et je ne pense pas qu'elle ait besoin de tout un système d'admin.
Flask me permet de développer une petite application rapidement et son intégration IA est moins lourde que Django.

### Modèle IA

J'ai choisi Gemma3:4b de Google pour sa créativité, sa rapidité d'exécution, son support multilangue, la possibilité de gérer du texte et des images et son nombre de tokens.

## Structure du projet

- Un backend développé en Flask
- Un frontend développé en React pour une intégration plus rapide de tailwind et des appels API

## Initialisation

### Installation des dépendances

#### Backend
Lancer un serveur virtuel python
```python
# si pas créé, tapez la commande qui suit
py -m venv .venv

# puis entrez cette commande
.venv/Scripts/activate
```
Installer les dépendances présentes dans le fichier "requirements.txt" à la racine du projet
```
pip install -r requirements.txt
```

#### Frontend
Se déplacer dans le dossier **frontend/** puis entrer la commande
```
npm install
```

### Configuration de la base de données

Remplacer le chemin de la db dans les fichiers suivant:
 - **backend/alembic.ini** : variable `sqlalchemy.url=` à la ligne 87
 - **backend/app.py** : variable `app.config['SQLALCHEMY_DATABASE_URI]=` à la ligne 6

### Récupération du modèle Gemma3:4b

 - Installer Ollama (https://ollama.com/download)
 - Dans une invite de commande, exécuter 
 ```
    ollama pull gemma3:4b
 ```

 ## Exécution

 - Dans un terminal, se positionner dans le dossier **backend** du projet et lancer la commande
 ```
py app.py
 ```
 - Dans un autre terminal, se positionner dans le dosser **frontend** du projet et lancer la commande
 ```
 npm run dev
 ```