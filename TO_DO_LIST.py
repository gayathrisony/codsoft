import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Information", "Tasks saved successfully.")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.read().splitlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task)
    except FileNotFoundError:
        return

root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("400x400")
root.configure(bg="lightblue")

frame_tasks = tk.Frame(root, bg="white")
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, border=0, bg="White", selectbackground="White")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", width=48, bg="yellow", fg="black", command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=48, bg="pink", fg="black", command=delete_task)
button_delete_task.pack()

button_save_tasks = tk.Button(root, text="Save Tasks", width=48, bg="orange", fg="black", command=save_tasks)
button_save_tasks.pack()

load_tasks()

root.mainloop()
