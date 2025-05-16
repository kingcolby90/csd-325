#colby king module 10 assignment#
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("King-ToDo")  # Changed title to last name-ToDo
root.geometry("300x400")
root.resizable(False, False)

# Create a frame to hold the todo list
todo_frame = ttk.Frame(root)
todo_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create scrollbar and listbox
scrollbar = ttk.Scrollbar(todo_frame)
scrollbar.pack(side="right", fill="y")

# Provide instructions for deletion in the label
instruction_label = ttk.Label(
    root, 
    text="Enter tasks below. Right-click a task to delete it.",  # Updated instruction for right-click
    wraplength=280
)
instruction_label.pack(pady=(0, 10))

# Configure colors for menu items
root.option_add('*Menu.activeBackground', '#4CAF50')  # Green
root.option_add('*Menu.activeForeground', 'white')
root.option_add('*Menu.background', '#F44336')  # Red (complementary to green)
root.option_add('*Menu.foreground', 'white')

# Using the colormap to change selection color
root.tk_setPalette(background='#f0f0f0')
root.option_add('*TCombobox*Listbox.selectBackground', '#4CAF50')
root.option_add('*TCombobox*Listbox.selectForeground', 'white')

# Create the todo list as a listbox
todo_list = tk.Listbox(
    todo_frame,
    height=15,
    width=40,
    selectmode="single",
    yscrollcommand=scrollbar.set,
    selectbackground="#4CAF50",
    selectforeground="white"
)
todo_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=todo_list.yview)

# Create entry for new tasks
task_entry = ttk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create the add task button
add_task_button = ttk.Button(
    root,
    text="Add Task",
    command=lambda: add_task()
)
add_task_button.pack(pady=(0, 10))

# Add task function
def add_task():
    task = task_entry.get().strip()
    if task:
        todo_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Modified to use right mouse button for deletion
def delete_task(event):
    try:
        index = todo_list.nearest(event.y)
        todo_list.delete(index)
    except tk.TclError:
        pass

# Exit function
def exit_program():
    root.destroy()

# Create menu bar with File menu and Exit option
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Bind right-click to delete_task instead of left-click
todo_list.bind("<Button-3>", delete_task)

# Focus on the entry box
task_entry.focus_set()

# Start the main event loop
root.mainloop()