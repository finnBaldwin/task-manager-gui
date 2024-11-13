Task Manager with Tkinter

A simple task manager application built in Python using Tkinter for the graphical user interface (GUI). This app allows users to add, view, delete, and mark tasks as completed. Tasks are saved persistently in a JSON file, so they remain between app sessions.

Features:
- Add New Task: Allows users to add a new task with a description.
- Mark Task as Completed: Lets users mark a task as completed.
- Delete Task: Allows users to delete a selected task from the list.
- Task Persistence: Tasks are saved to a tasks.json file, so they persist across app restarts.
- Simple, User-Friendly Interface: Built with Tkinter, providing an intuitive graphical interface.

Requirements:
- Python 3.x (tested with Python 3.8+)
- Tkinter (usually comes pre-installed with Python)

Installation:
1. Clone the Repository or download the source code:

   git clone https://github.com/finnBaldwin/task-manager-tkinter-python3.git
   cd task-manager-tkinter

2. Install Python: Ensure you have Python 3.x installed. You can check by running:

   python --version

3. Install Tkinter (if not already installed): For most Python installations, Tkinter comes pre-installed. If it's not, you can install it using your package manager:

   - On Ubuntu:
     sudo apt-get install python3-tk
   - On macOS:
     Tkinter should come with the default Python installation.
   - On Windows:
     Tkinter is included by default with Python.

Usage:
1. Run the Task Manager:

   In your terminal or command prompt, run the following command to start the task manager application:

   python task_manager_gui.py

2. Interacting with the Application:
   - Add a Task: Type a task description in the input field and click the "Add Task" button to add it to the list.
   - Mark Task as Completed: Select a task from the list and click the "Mark as Completed" button to update its status.
   - Delete a Task: Select a task from the list and click the "Delete Task" button to remove it.
   - Tasks are saved to a tasks.json file, so they will persist across app restarts.

Task List Display:
The task list shows each task's:
- ID
- Description
- Status (Pending or Completed)

File Structure:
task-manager-tkinter/
├── task_manager_gui.py  # Main Python script with Tkinter GUI
├── tasks.json           # JSON file storing tasks (created automatically)
└── README.md            # This README file

How It Works:
- Persistent Storage: The application uses a tasks.json file to save and load tasks. This file is created automatically if it doesn’t exist, and it gets updated whenever a task is added, deleted, or modified.
- Tkinter GUI: The app uses Tkinter to provide a simple graphical interface. The main window has:
  - An Entry widget to input new tasks.
  - A Listbox to display tasks.
  - Buttons to add tasks, mark tasks as completed, and delete tasks.

Key Functions:
- load_tasks(): Loads tasks from the tasks.json file into the application.
- save_tasks(): Saves the current list of tasks to the tasks.json file.
- add_task(): Adds a new task with the description entered in the text box.
- mark_completed(): Marks a selected task as completed.
- delete_task(): Deletes a selected task from the list.
- update_task_list(): Updates the Listbox to reflect the current tasks.

Contributing:
Feel free to fork this repository and submit pull requests. Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue.

License:
This project is open-source and available under the MIT License.