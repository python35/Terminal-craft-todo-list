import json
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, DataTable, Button
from textual.containers import VerticalScroll, Vertical
from textual.screen import Screen
from textual.reactive import reactive # Voor dynamische veranderingen in de UI

# Bestand waar taken worden opgeslagen
TASKS_FILE = Path("tasks.json")

class Task:
    """Representeert een enkele To-Do taak."""
    def __init__(self, id: int, text: str, completed: bool = False):
        self.id = id
        self.text = text
        self.completed = completed

    def to_dict(self):
        """Converteert de taak naar een dictionary voor opslag."""
        return {"id": self.id, "text": self.text, "completed": self.completed}

    @classmethod
    def from_dict(cls, data: dict):
        """Maakt een Task object van een dictionary."""
        return cls(data["id"], data["text"], data["completed"])

class MainScreen(Screen):
    """Het hoofdscherm van de applicatie."""

    # Definieer sneltoetsen voor acties
    BINDINGS = [
        ("a", "add_task_prompt", "Add Task"),
        ("d", "delete_selected_task", "Delete Selected"),
        ("c", "toggle_selected_task_completion", "Toggle Complete"),
        ("v", "toggle_view_completed", "Toggle View Completed"),
        ("q", "quit", "Quit"),
        ("escape", "clear_selection", "Clear Selection") # Optioneel: deselecteer rij
    ]

    # Reactive variabele om te bepalen of voltooide taken worden getoond
    show_completed = reactive(True)

    def compose(self) -> ComposeResult:
        """Creëert de child widgets voor dit scherm."""
        yield Header()
        with VerticalScroll(id="task-list-container"): # Container voor de takenlijst
            self.task_table = DataTable(classes="task-list")
            self.task_table.add_columns("ID", "Taak Beschrijving", "Status")
            yield self.task_table
        yield Input(placeholder="Nieuwe taak toevoegen...", id="task_input")
        yield Footer()

    def on_mount(self) -> None:
        """Wordt aangeroepen wanneer het scherm is 'gemonteerd'."""
        self.app.load_tasks() # Laad taken bij het opstarten
        self.update_task_table() # Update de weergave

        # Focus op de input field bij het opstarten
        self.query_one("#task_input", Input).focus()

    def watch_show_completed(self, show_completed: bool) -> None:
        """Observer voor veranderingen in show_completed, om de tabel bij te werken."""
        self.update_task_table()
        self.notify(f"Voltooide taken tonen: {show_completed}", timeout=2)


    def update_task_table(self):
        """Werkt de DataTable bij met de huidige taken."""
        self.task_table.clear() # Leeg de huidige tabel
        rows = []
        # Sorteer taken op ID, zodat ze consistent zijn
        sorted_tasks = sorted(self.app.tasks, key=lambda t: t.id)
        
        for task in sorted_tasks:
            if self.show_completed or not task.completed:
                status = "[green bold]VOLTOOID[/green bold]" if task.completed else "[red bold]OPEN[/red bold]"
                task_text = f"[strike]{task.text}[/strike]" if task.completed else task.text
                rows.append((task.id, task_text, status))
        
        self.task_table.add_rows(rows)
        # Selecteer de eerste rij als er rijen zijn, voor een betere UX
        if rows:
            # We moeten de focus van de DataTable instellen op een specifieke cel
            # om de cursor te verplaatsen. De makkelijkste manier is de eerste cel
            # van de eerste rij te selecteren.
            self.task_table.focus() # Zorg dat de tabel zelf focus heeft
            self.task_table.move_cursor(row=0, column=0) # Verplaats de cursor naar de eerste cel

    # ------ Acties die door sneltoetsen worden aangeroepen ------
    
    def action_add_task_prompt(self) -> None:
        """Focust op het inputveld om een taak toe te voegen."""
        self.query_one("#task_input", Input).focus()
    
    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Wordt aangeroepen wanneer de gebruiker Enter drukt in het invoerveld."""
        task_text = event.value.strip()
        if task_text:
            self.app.add_task(task_text)
            event.control.value = "" # Leeg het invoerveld
            self.update_task_table()
        else:
            self.notify("Taak kan niet leeg zijn!", severity="warning")
        event.control.focus() # Houd de focus op het invoerveld

    def action_delete_selected_task(self) -> None:
        """Verwijdert de geselecteerde taak."""
        if self.task_table.cursor_row is not None:
            # Haal de ID op van de geselecteerde rij
            selected_row_data = self.task_table.get_row_at(self.task_table.cursor_row)
            if selected_row_data:
                task_id_to_delete = selected_row_data[0] # ID is de eerste kolom
                self.app.delete_task(task_id_to_delete)
                self.update_task_table()
                self.notify(f"Taak {task_id_to_delete} verwijderd.")
            else:
                self.notify("Geen geldige taak geselecteerd.", severity="warning")
        else:
            self.notify("Geen taak geselecteerd om te verwijderen.", severity="warning")

    def action_toggle_selected_task_completion(self) -> None:
        """Wijzigt de voltooiingsstatus van de geselecteerde taak."""
        if self.task_table.cursor_row is not None:
            selected_row_data = self.task_table.get_row_at(self.task_table.cursor_row)
            if selected_row_data:
                task_id_to_toggle = selected_row_data[0]
                self.app.toggle_task_completion(task_id_to_toggle)
                self.update_task_table()
                self.notify(f"Status taak {task_id_to_toggle} gewijzigd.")
            else:
                self.notify("Geen geldige taak geselecteerd.", severity="warning")
        else:
            self.notify("Geen taak geselecteerd om de status te wijzigen.", severity="warning")
            
    def action_toggle_view_completed(self) -> None:
        """Schakelt het tonen van voltooide taken aan/uit."""
        self.show_completed = not self.show_completed
        # De 'watch_show_completed' methode zal de update_task_table() al aanroepen

    def action_clear_selection(self) -> None:
        """Deselecteert de huidige rij in de tabel."""
        # Probeer de highlight te verwijderen.
        # Als dit ook een fout geeft, moeten we de regel helemaal weglaten.
        self.task_table.highlight_cell(None) # Dit is een poging
        self.notify("Selectie gewist.", timeout=1)

    def action_quit(self) -> None:
        """Sluit de applicatie af."""
        self.app.exit()


class TodoApp(App):
    """De hoofd Textual applicatie klasse."""
    
    CSS_PATH = "todo.css" # Link naar het CSS-bestand
    SCREENS = {"main": MainScreen} # <-- Let op: GEEN haakjes () achter MainScreen

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def on_mount(self) -> None:
        """Initialiseer en toon het hoofdscherm bij het opstarten van de app."""
        self.push_screen("main")

    def load_tasks(self) -> None:
        """Laadt taken uit het JSON-bestand."""
        if TASKS_FILE.exists():
            try:
                with open(TASKS_FILE, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(d) for d in data]
                    if self.tasks:
                        # Vind de hoogste ID om ervoor te zorgen dat nieuwe ID's uniek zijn
                        self.next_id = max(task.id for task in self.tasks) + 1
                    self.notify(f"Taken geladen van {TASKS_FILE.name}")
            except json.JSONDecodeError:
                self.notify(f"Fout bij het lezen van {TASKS_FILE.name}. Start met lege lijst.", severity="error")
            except Exception as e:
                self.notify(f"Onverwachte fout bij laden: {e}", severity="error")
        else:
            self.notify(f"{TASKS_FILE.name} niet gevonden. Start met lege lijst.", severity="warning")

    def save_tasks(self) -> None:
        """Slaat taken op naar het JSON-bestand."""
        try:
            with open(TASKS_FILE, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=4)
            # self.notify(f"Taken opgeslagen naar {TASKS_FILE.name}", timeout=1) # Kan storend zijn
        except Exception as e:
            self.notify(f"Fout bij opslaan van taken: {e}", severity="error")

    def add_task(self, text: str) -> None:
        """Voegt een nieuwe taak toe."""
        new_task = Task(self.next_id, text)
        self.tasks.append(new_task)
        self.next_id += 1
        self.save_tasks()

    def delete_task(self, task_id: int) -> None:
        """Verwijdert een taak op basis van ID."""
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) < original_len:
            self.save_tasks()
        else:
            self.notify(f"Taak {task_id} niet gevonden.", severity="warning")


    def toggle_task_completion(self, task_id: int) -> None:
        """Wijzigt de voltooiingsstatus van een taak."""
        found = False
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                found = True
                break
        if found:
            self.save_tasks()
        else:
            self.notify(f"Taak {task_id} niet gevonden.", severity="warning")


if __name__ == "__main__":
    app = TodoApp()
    app.run()