import tkinter as tk
from tkinter import ttk

def create_add_file_button(root, command):
    button = tk.Button(root, text="Add Files", command=command)
    button.pack(pady=10)
    return button

def create_file_listbox(root):
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
    listbox.pack(pady=10)
    return listbox

def create_remove_file_button(root, command):
    button = tk.Button(root, text="Remove Selected Files", command=command)
    button.pack(pady=10)
    return button

def create_zip_button(root, command):
    button = tk.Button(root, text="Create Zip", command=command)
    button.pack(pady=10)
    return button

def create_progress_bar(root):
    progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
    progress_bar.pack(pady=10)
    return progress_bar
