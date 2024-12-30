# ⏰ Timer 
Un script Python interactif utilisant la bibliothèque `rich` pour gérer des cycles de travail et de pause. Ce script est utile pour augmenter la productivité en respectant des périodes de travail concentré et de courtes pauses, basé sur des principes tels que la méthode Pomodoro.

## Fonctionnalités
- **Cycles de travail et de pause** : Configurez un temps de travail et une pause est automatiquement calculée (1/5 du temps de travail).
- **Notifications Pushover** : Recevez des notifications push lorsque le cycle de travail ou de pause est terminé.
- **Interface utilisateur interactive** : Utilisation de la bibliothèque `rich` pour une interface utilisateur élégante dans le terminal.
- **Commande pour quitter** : Arrêtez le script à tout moment en entrant `q`.

## Installation
### Prérequis 
- Python 3.8 ou version supérieure
- Installez les bibliothèques nécessaires :
```bash
pip install -r requirements.txt
```
- Un compte [PushOver](https://pushover.net/) avec un **user key** et un **API token**.

### Cloner le projet
```bash
git clone https://github.com/votre-utilisateur/timer.git
cd timer
```

### Configuration
Créez un fichier `api.py` dans le dossier principal et ajoutez vos clés d'API Pushover comme suit :
```python
KEY = "votre_user_key"
TOKEN = "votre_api_token"
```

## Utilisation
Exécutez le script avec Python :
```bash
python3 main.py
```
### Commandes interactives
- Entrez un **temps de travail en minutes** pour démarrer un cycle.
- Le script affiche :
  - Temps de travail restant
  - Temps de pause restant
- **Entrez** `q` pour quitter le programme.

## Fonctionnalités détaillées
### Notifications Pushover
Lorsque le cycle de travail ou de pause est terminé, une notification est envoyée à l'aide de l'API Pushover.

### Temps de pause automatique
Le temps de pause est calculé automatiquement comme étant **1/5** du temps de travail.

### Interface utilisateur enrichie
Grâce à la bibliothèque `rich`, les messages du terminal sont colorés et formatés pour une meilleure lisibilité.

## Exemple
### Cycle de travail
```bash
Entrez le temps de travail en minutes (ou 'q' pour quitter) : 25
Temps de travail : 25 minutes
Temps de travail - Temps restant : 24:59
...
Temps de travail terminé !
Temps de pause : 5 minutes
Temps de pause - Temps restant : 04:59
...
Cycle terminé ! Vous pouvez commencer un nouveau cycle ou quitter.
```

## Contribution
Les contributions sont les bienvenues ! N'hésitez pas à soumettre une pull request ou à ouvrir une issue.

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.