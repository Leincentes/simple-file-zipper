import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

class FileZipper:
    def __init__(self, root):
        self.root = root
        self.root.title("File Zipper")
        
        self.file_list = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Add file button
        self.add_file_button = tk.Button(self.root, text="Add Files", command=self.add_files)
        self.add_file_button.pack(pady=10)
        
        # File listbox
        self.file_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=50, height=10)
        self.file_listbox.pack(pady=10)
        
        # Remove file button
        self.remove_file_button = tk.Button(self.root, text="Remove Selected Files", command=self.remove_files)
        self.remove_file_button.pack(pady=10)
        
        # Zip button
        self.zip_button = tk.Button(self.root, text="Create Zip", command=self.create_zip)
        self.zip_button.pack(pady=10)
        
    def add_files(self):
        files = filedialog.askopenfilenames(title="Select Files")
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
        
        try:
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in self.file_list:
                    zipf.write(file, os.path.basename(file))
                    
            messagebox.showinfo("Success", f"Files successfully zipped into {zip_filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FileZipper(root)
    root.mainloop()
