import tkinter as tk
from file_zipper import FileZipper

def main():
    root = tk.Tk()
    app = FileZipper(root)
    root.mainloop()

if __name__ == "__main__":
    main()
