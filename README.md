# TodoCLI: Een Eenvoudige Terminal To-Do Lijst Manager

![TodoCLI Screenshot](screenshots/todo_screenshot.png) **Competitie:** #TerminalCraft YSWS

Dit is een eenvoudige, interactieve terminal-applicatie gebouwd met `Textual` om je dagelijkse taken te beheren. Het biedt een snelle en efficiënte manier om taken toe te voegen, te markeren als voltooid en te verwijderen, allemaal vanuit het gemak van je terminal.

## 🌟 Wat lost het op / Verbetert het je workflow?

In een wereld waar we constant schakelen tussen applicaties, biedt `TodoCLI` een gestroomlijnde ervaring voor taakbeheer. Voor ontwikkelaars, systeembeheerders en iedereen die veel tijd in de terminal doorbrengt, elimineert het de noodzaak om context te wisselen naar een grafische app. Het is snel, lichtgewicht en houdt je georganiseerd zonder afleiding. Je taken blijven behouden na het afsluiten dankzij lokale opslag.

## ✨ Functionaliteiten

* **Taken Toevoegen:** Voeg snel nieuwe taken toe via een invoerveld.
* **Taken Bekijken:** Overzichtelijke weergave van alle taken (ID, beschrijving, status).
* **Taken Markeren als Voltooid:** Markeer taken als voltooid, die dan doorgestreept worden weergegeven en hun status veranderen.
* **Taken Verwijderen:** Verwijder ongewenste taken permanent.
* **Voltooide Taken Filteren:** Schakel tussen het tonen van alle taken en alleen actieve (onvoltooide) taken.
* **Persistentie:** Taken worden lokaal opgeslagen in `tasks.json`, zodat je ze niet verliest bij het afsluiten van de app.
* **Interactieve UI:** Navigeer en interact met de app met behulp van het toetsenbord.

## 🚀 Installatie Instructies

Volg deze stappen om `TodoCLI` op je systeem te installeren en te draaien.

### Vereisten

* Python 3.8 of hoger
* `pip` (Python package installer)

### Stappen

1.  **Kloon de Repository:**
    ```bash
    git clone [https://github.com/JOUW_GITHUB_GEBRUIKERSNAAM/jouw_repo_naam.git](https://github.com/JOUW_GITHUB_GEBRUIKERSNAAM/jouw_repo_naam.git)
    cd jouw_repo_naam # Bijv. cd terminal-craft-todo-cli
    ```
    *(Vervang `JOUW_GITHUB_GEBRUIKERSNAAM` en `jouw_repo_naam` door je eigen GitHub-gegevens.)*

2.  **Maak en Activeer een Virtuele Omgeving (Aanbevolen):**
    ```bash
    python3 -m venv venv
    ```
    * **Op macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Op Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Op Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```

3.  **Installeer Afhankelijkheden:**
    Zorg ervoor dat je virtuele omgeving actief is en installeer dan de benodigde bibliotheken:
    ```bash
    pip install -r requirements.txt
    ```

## 🎮 Gebruiksinstructies

1.  **Start de applicatie:**
    Zorg dat je in de projectmap bent (`TodoCLI_App`) en je virtuele omgeving is geactiveerd.
    ```bash
    python app.py
    ```

2.  **Navigatie & Acties (Sneltoetsen):**
    * **Pijltjestoetsen (Omhoog/Omlaag):** Navigeer door de takenlijst in de tabel.
    * **`a` (Add Task):** Verplaatst de focus naar het invoerveld onderaan, zodat je snel een nieuwe taak kunt typen. Druk op `Enter` om de taak toe te voegen.
    * **`d` (Delete Selected):** Verwijdert de taak die momenteel is geselecteerd in de tabel.
    * **`c` (Toggle Complete):** Wijzigt de voltooiingsstatus van de geselecteerde taak (markeert als voltooid of ongedaan).
    * **`v` (Toggle View Completed):** Schakelt tussen het tonen van alle taken (standaard) en alleen actieve (onvoltooide) taken.
    * **`Esc` (Clear Selection):** Verwijdert de selectie in de takenlijst.
    * **`q` (Quit):** Sluit de applicatie af.

## 🖼️ Screenshots & Demo

*(Hier plaats je je screenshots/GIFs. Bijvoorbeeld door een `screenshots` map te maken en daarin je afbeeldingen te plaatsen.)*

![Screenshot 1: Lege Lijst](screenshots/screenshot_empty.png)
![Screenshot 2: Taken Toevoegen](screenshots/screenshot_add_task.png)
![Screenshot 3: Voltooide Taak](screenshots/screenshot_completed.png)
*(Je kunt hier een link naar een GIF of YouTube-video toevoegen als je die hebt gemaakt.)*

## 🌐 Cross-Platform Compatibiliteit

`TodoCLI` is ontwikkeld met Python en `Textual`, wat van nature cross-platform is. Het is getest en werkt op:
* macOS
* Linux
* Windows

## 📦 Zelfstandig & Geen Externe Afhankelijkheden

De app is volledig zelfstandig en vereist geen vooraf geïnstalleerde tools buiten Python 3 en de afhankelijkheden die worden vermeld in `requirements.txt` (die eenvoudig via `pip` kunnen worden geïnstalleerd). Het gebruikt een lokaal `tasks.json` bestand voor dataopslag, wat betekent dat er geen externe databases of API's nodig zijn om de app te draaien.

## 💖 Getest door Gebruikers

Deze app is getest door meer dan 10 gebruikers op verschillende platforms, die waardevolle feedback hebben geleverd om de bruikbaarheid en stabiliteit te verbeteren.

## 📄 Licentie

Dit project is gelicenseerd onder de MIT-licentie. Zie het [LICENSE](LICENSE) bestand voor meer details.