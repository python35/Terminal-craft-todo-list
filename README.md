# TodoCLI: A Simple Terminal To-Do List Manager

**Contest:** #TerminalCraft YSWS

This is a straightforward, interactive terminal application built with `Textual` to help you manage your daily tasks. It offers a quick and efficient way to add, mark as complete, and delete tasks, all from the convenience of your terminal.

## 🌟 What problem does it solve / How does it improve your workflow?

In a world where we constantly switch between applications, `TodoCLI` provides a streamlined experience for task management. For developers, system administrators, and anyone who spends a lot of time in the terminal, it eliminates the need to context-switch to a graphical app. It's fast, lightweight, and keeps you organized without distractions. Your tasks persist after closing the application thanks to local storage.

## ✨ Features

* **Add Tasks:** Quickly add new tasks via an input field.
* **View Tasks:** Clear overview of all tasks (ID, description, status).
* **Mark Tasks as Complete:** Mark tasks as complete, which are then displayed as struck-through and change their status.
* **Delete Tasks:** Permanently remove unwanted tasks.
* **Filter Completed Tasks:** Toggle between showing all tasks and only active (incomplete) tasks.
* **Persistence:** Tasks are saved locally in `tasks.json`, so you don't lose them when closing the app.
* **Interactive UI:** Navigate and interact with the app using the keyboard.

## 🚀 Installation Instructions

Follow these steps to install and run `TodoCLI` on your system.

### Requirements

* Python 3.8 or higher
* `pip` (Python package installer)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/runebobbaers/terminal-craft-todo-cli.git](https://github.com/runebobbaers/terminal-craft-todo-cli.git)
    cd terminal-craft-todo-cli
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **On Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```

3.  **Install Dependencies:**
    Ensure your virtual environment is active, then install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

    ## 🖼️ Screenshots & Demo

    Here are some screenshots showcasing the TodoCLI application:

    ![Screenshot of an empty task list](Schermafbeelding 2025-06-15 om 12.21.27.png)
    *An empty task list, ready for your input.*

    ![Screenshot with tasks added](Schermafbeelding 2025-06-15 om 12.24.18.png)
    *Tasks added and managed within the application.*

## 🎮 Usage Instructions

1.  **Start the application:**
    Make sure you are in the project directory (`terminal-craft-todo-cli`) and your virtual environment is activated.
    ```bash
    python app.py
    ```

2.  **Navigation & Actions (Hotkeys):**
    * **Arrow Keys (Up/Down):** Navigate through the task list in the table.
    * **`a` (Add Task):** Moves focus to the input field at the bottom, allowing you to quickly type a new task. Press `Enter` to add the task.
    * **`d` (Delete Selected):** Deletes the task currently selected in the table.
    * **`c` (Toggle Complete):** Changes the completion status of the selected task (marks as complete or incomplete).
    * **`v` (Toggle View Completed):** Toggles between showing all tasks (default) and only active (incomplete) tasks.
    * **`Esc` (Clear Selection):** Clears the selection in the task list.
    * **`q` (Quit):** Exits the application.

## 🖼️ Screenshots & Demo

*(Currently, there are no screenshots available. Please add your screenshots to the `screenshots` folder and link them here to showcase your application!)*

## 🌐 Cross-Platform Compatibility

`TodoCLI` is developed with Python and `Textual`, which is inherently cross-platform. It is designed to work on:
* macOS
* Linux
* Windows

## 📦 Standalone & No External Dependencies

The application is fully self-contained and does not require any pre-installed tools beyond Python 3 and the dependencies listed in `requirements.txt` (which can be easily installed via `pip`). It uses a local `tasks.json` file for data storage, meaning no external databases or APIs are needed to run the app.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
