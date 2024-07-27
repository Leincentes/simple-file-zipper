import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
import zipfile
import os
import threading

class FileZipper:
    def __init__(self, root):
        self.root = root
        self.root.title("File Zipper")
        
        self.file_list = []
        
        self.create_widgets()
        
    def create_widgets(self):
        from .ui import create_add_file_button, create_file_listbox, create_remove_file_button, create_zip_button, create_progress_bar

        # Add file button
        self.add_file_button = create_add_file_button(self.root, self.add_files)
        
        # File listbox
        self.file_listbox = create_file_listbox(self.root)
        
        # Remove file button
        self.remove_file_button = create_remove_file_button(self.root, self.remove_files)
        
        # Zip button
        self.zip_button = create_zip_button(self.root, self.create_zip)
        
        # Progress bar
        self.progress_bar = create_progress_bar(self.root)
        
    def add_files(self):
        file_types = [("Text files", "*.txt"), ("Python files", "*.py"), ("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")]
        files = filedialog.askopenfilenames(title="Select Files", filetypes=file_types)
        for file in files:
            if file not in self.file_list:
                self.file_list.append(file)
                self.file_listbox.insert(tk.END, file)
                
    def remove_files(self):
        selected_files = self.file_listbox.curselection()
        for index in reversed(selected_files):
            self.file_listbox.delete(index)
            del self.file_list[index]
        
    def create_zip(self):
        if not self.file_list:
            messagebox.showwarning("No files selected", "Please add files to zip.")
            return
        
        zip_filename = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("Zip files", "*.zip")])
        if not zip_filename:
            return
        
        # Ask for custom zip file name
        zip_filename = simpledialog.askstring("Input", "Enter the name of the zip file:", initialvalue=os.path.basename(zip_filename))
        if not zip_filename:
            return
        zip_filename = f"{os.path.splitext(zip_filename)[0]}.zip"

        # Start zip creation in a separate thread
        threading.Thread(target=self._create_zip_file, args=(zip_filename,), daemon=True).start()
        
    def _create_zip_file(self, zip_filename):
        from .utils import update_progress_bar
        try:
            total_files = len(self.file_list)
            self.progress_bar['maximum'] = total_files

            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for index, file in enumerate(self.file_list):
                    zipf.write(file, os.path.basename(file))
                    update_progress_bar(self.progress_bar, index + 1, self.root)

            messagebox.showinfo("Success", f"Files successfully zipped into {zip_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.progress_bar['value'] = 0
