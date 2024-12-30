from rich.console import Console
from rich.text import Text
import time
import requests
import api

console = Console()

# pushover
user_key = api.KEY
api_token = api.TOKEN

def send_push_notification(title, message):
    payload = {
        "token": api_token,
        "user": user_key,
        "title": title,
        "message": message,
    }
    response = response = requests.post("https://api.pushover.net/1/messages.json", data=payload)
    """
    if response.status_code == 200:
        print(Fore.GREEN + "Notification envoyée avec succès.")
    else:
        print(Fore.RED + f"Erreur lors de l'envoi de la notification : {response.status_code} - {response.text}")
    """

def start_timer():
    while True:
        try:
            # Demander le temps de travail
            work_minutes = console.input("[cyan]Entrez le temps de travail en minutes (ou 'q' pour quitter) : [/cyan]")
            if work_minutes.lower() == 'q':
                console.print("[bold green]Programme terminé. Bonne journée ![/bold green]")
                break

            work_minutes = int(work_minutes)
            work_time = work_minutes * 60  # Convertir en secondes
            pause_time = work_time // 5    # Temps de pause (1/5 du temps de travail)

            console.print(f"\n[bold blue]Temps de travail : {work_minutes} minutes[/bold blue]")
            countdown_timer(work_time, "[bold blue]Temps de travail[/bold blue]")

            console.print(f"\n[bold magenta]Temps de pause : {pause_time // 60} minutes[/bold magenta]")
            countdown_timer(pause_time, "[bold magenta]Temps de pause[/bold magenta]")

            console.print("\n[bold yellow]Cycle terminé ! Vous pouvez commencer un nouveau cycle ou quitter.[/bold yellow]")
        except ValueError:
            console.print("[bold red]Erreur : Veuillez entrer un nombre valide ou 'q' pour quitter.[/bold red]")

def countdown_timer(seconds, phase):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        console.print(f"{phase} - Temps restant : {mins:02}:{secs:02}", end="", justify="left", highlight=False)  # Désactive la nouvelle ligne
        time.sleep(1)
        console.clear()  # Efface la console pour mettre à jour la ligne actuelle
    console.print(f"\n{phase} [bold green]terminé ![/bold green]")
    send_push_notification("Timer", "Time's up !")

if __name__ == "__main__":
    start_timer()
    