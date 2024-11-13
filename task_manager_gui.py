import tkinter as tk
from tkinter import messagebox
import json
import os

# Load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

# Save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add task to the list
def add_task():
    task_desc = task_entry.get()
    if task_desc:
        tasks.append({"id": len(tasks) + 1, "description": task_desc, "status": "pending"})
        task_entry.delete(0, tk.END)
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

# Mark task as completed
def mark_completed():
    try:
        selected_task = task_listbox.curselection()[0]
        task_id = task_listbox.get(selected_task).split(" - ")[0]
        for task in tasks:
            if str(task["id"]) == task_id:
                task["status"] = "completed"
                update_task_list()
                save_tasks(tasks)
                break
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Delete a task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_id = task_listbox.get(selected_task).split(" - ")[0]
        tasks[:] = [task for task in tasks if str(task["id"]) != task_id]
        update_task_list()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Update the task listbox display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["status"] == "completed" else "✘"
        task_listbox.insert(tk.END, f"{task['id']} - {task['description']} - {status}")

# Create the main application window
root = tk.Tk()
root.title("Task Manager")

# Load tasks when the app starts
tasks = load_tasks()

# Create the task listbox and scroll bar
task_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
task_listbox.pack(pady=20)

# Add initial tasks to the listbox
update_task_list()

# Task entry input
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Mark as completed button
mark_button = tk.Button(root, text="Mark as Completed", width=20, command=mark_completed)
mark_button.pack(pady=5)

# Delete task button
delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
