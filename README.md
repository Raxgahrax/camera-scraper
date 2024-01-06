Ce projet est un scraper Python pour récupérer des adresses IP et des flux en direct à partir du site Insecam.

## Description

Ce scraper utilise des requêtes HTTP pour récupérer des adresses IP et des flux en direct provenant du site www.insecam.org en fonction des codes de pays spécifiés.

## Fonctionnement

1. **Dépendances**
   - Ce projet utilise les librairies Python suivantes :
     - `requests`
     - `colorama`
     - `user_agent`
     - `concurrent.futures`

2. **Installation**
   - Assurez-vous d'avoir Python 3 installé.
   - Clonez ce dépôt : `git clone https://github.com/Raxgahrax/camera-scraper.git`
   - Installez les dépendances manuellement : `pip3 install requests colorama user_agent concurrent.futures`

3. **Utilisation**
   - Exécutez le fichier avec `python3 main.py`.
   - Modifiez la variable `Country` pour scanner un pays spécifique ou utilisez `'All'` pour scanner tous les pays.

4. **Avertissement**
   - Ce projet est uniquement destiné à des fins éducatives.
   - Respectez les politiques d'utilisation du site www.insecam.org lors de l'exécution de ce code.

## Détails Supplémentaires

### Structure du Projet

Le script utilise une structure simple sans sous-dossiers supplémentaires. Les résultats de la collecte sont stockés dans le dossier `output_countries`.

### Modification de la variable `Country`

La variable `Country` permet de spécifier le pays à scanner. Changez sa valeur pour un code de pays spécifique ou utilisez `'All'` pour scanner tous les pays disponibles.

### Gestion des Résultats

Les adresses IP collectées sont enregistrées dans des fichiers texte spécifiques aux pays. Ils sont stockés dans le dossier `output_countries`, organisés par pays.

### Utilisation de la Coloration de Console

La librairie `colorama` est utilisée pour colorer la sortie de la console. Les flux en direct, les adresses valides, etc., sont mis en évidence pour une meilleure lisibilité lors du utilisation via un terminal.

### Compréhension des Dépendances

- `requests` : Gestion des requêtes HTTP pour récupérer les données du site.
- `colorama` : Coloration de la sortie console pour une meilleure présentation.
- `user_agent` : Génération aléatoire d'User-Agents pour les requêtes.
- `concurrent.futures` : Exécution concurrente des tâches pour une efficacité accrue.

## Optimisations

- Implémentation du Tor : Pour améliorer la confidentialité et l'anonymat lors des requêtes, une option d'implémentation du réseau Tor serait à mettre en place.

## Avertissement Éthique

Ce projet est un scraper Python pour récupérer des adresses IP et des flux en direct à partir du site Insecam.

## Description

Ce scraper utilise des requêtes HTTP pour récupérer des adresses IP et des flux en direct provenant du site www.insecam.org en fonction des codes de pays spécifiés.

## Fonctionnement

1. **Dépendances**
   - Ce projet utilise les librairies Python suivantes :
     - `requests`
     - `colorama`
     - `user_agent`
     - `concurrent.futures`

2. **Installation**
   - Assurez-vous d'avoir Python 3 installé.
   - Clonez ce dépôt : `git clone https://github.com/Raxgahrax/camera-scraper.git`
   - Installez les dépendances manuellement : `pip3 install requests colorama user_agent concurrent.futures`

3. **Utilisation**
   - Exécutez le fichier avec `python3 main.py`.
   - Modifiez la variable `Country` pour scanner un pays spécifique ou utilisez `'All'` pour scanner tous les pays.

4. **Avertissement**
   - Ce projet est uniquement destiné à des fins éducatives.
   - Respectez les politiques d'utilisation du site www.insecam.org lors de l'exécution de ce code.

## Détails Supplémentaires

### Structure du Projet

Le script utilise une structure simple sans sous-dossiers supplémentaires. Les résultats de la collecte sont stockés dans le dossier `output_countries`.

### Modification de la variable `Country`

La variable `Country` permet de spécifier le pays à scanner. Changez sa valeur pour un code de pays spécifique ou utilisez `'All'` pour scanner tous les pays disponibles.

### Gestion des Résultats

Les adresses IP collectées sont enregistrées dans des fichiers texte spécifiques aux pays. Ils sont stockés dans le dossier `output_countries`, organisés par pays.

### Utilisation de la Coloration de Console

La librairie `colorama` est utilisée pour colorer la sortie de la console. Les flux en direct, les adresses valides, etc., sont mis en évidence pour une meilleure lisibilité lors du utilisation via un terminal.

### Compréhension des Dépendances

- `requests` : Gestion des requêtes HTTP pour récupérer les données du site.
- `colorama` : Coloration de la sortie console pour une meilleure présentation.
- `user_agent` : Génération aléatoire d'User-Agents pour les requêtes.
- `concurrent.futures` : Exécution concurrente des tâches pour une efficacité accrue.

## Optimisations

- Implémentation du Tor : Pour améliorer la confidentialité et l'anonymat lors des requêtes, une option d'implémentation du réseau Tor serait à mettre en place.

## Avertissement Éthique

- Assurez-vous d'utiliser cet outil de manière responsable et éthique.
- Il est important de respecter les politiques d'utilisation du site www.insecam.org lors de l'exécution de ce script.
