# Wordle (Devine le mot)

## Binôme
- Alexy Catelle 
- Xareni Galindo

## Le but

- Deviner un mot entre 2 et 21 lettres en 6 tentatives maximum.

## Règles

### Longueur
- Le joueur choisi la taille du mot qu'il souhaite deviner.
- Chaque tentative doit être de la même longueur que le mot à deviner.

### Tentatives 
Vous disposez de 6 tentatives maximum pour trouver le mot.

### Indices
 Vous optenez des indices à chaque essai par la couleur des lettres affichées :
- Vert : la lettre se trouve dans le mot à la bonne place.
- Jaune : la lettre se trouve dans le mot mais à la mauvaise place.
- Gris : la lettre ne fait pas partie du mot caché.

## Exemple 

- mot cible : tiret
- mot tentative : texte

![](/attachments/exemple.png)

## Commandes

Utilisation du clavier et de la souris.


## Instructions

- Installer les requirements : ``python -m pip install -r requirements.txt``
- Version terminal : ``python terminal_version/app.py``
- Version interface : ``python main.py``


## Schema architecture

![](/attachments/schema_arch.png)
## Pistes d'amélioration

- Vérification que le mot proposé par l'utlisateur est un mot valide de la langue française.

- Ajouter la possibilité de choisir la langue du jeu.

- Ajouter le clavier visuel sur l'interface.

- Sauvegarde des scores.

