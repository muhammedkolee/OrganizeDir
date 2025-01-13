import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Organize Directory")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # App Title
        self.title_label = tk.Label(root, text="Organize Dir.", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Button of Select the directory
        self.label = tk.Label(root, text="Select the directory:", font=("Arial", 12))
        self.label.pack(pady=5)
        
        self.select_button = ttk.Button(root, text="Select", command=self.select_folder)
        self.select_button.pack(pady=5)
        
        # Show path of selected directory
        self.selected_folder_label = tk.Label(root, text="Selected Directory: None", font=("Arial", 10), wraplength=550, justify="center")
        self.selected_folder_label.pack(pady=5)
        
        # Button of manage and list directory
        self.list_button = ttk.Button(root, text="List the inside of directory", command=self.list_folder_contents)
        self.list_button.pack(pady=5)
        
        self.organize_button = ttk.Button(root, text="Organize the directory", command=self.organize_files)
        self.organize_button.pack(pady=5)
        
        # Shown directories or documents in the directory
        self.text_area = tk.Text(root, width=70, height=20, state="disabled", font=("Courier New", 10))
        self.text_area.pack(pady=10)
        
        # Path of Directory
        self.folder_path = ""
        
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.selected_folder_label.config(text=f"Selected Directory: {self.folder_path}")
            messagebox.showinfo("Selected Directory", f"Selected Directory: {self.folder_path}")
        
    def organize_files(self):
        if not self.folder_path:
            messagebox.showwarning("Warning", "Please, select directory!")
            return
        
        extensions = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".heif", ".heic", ".raw", ".nef", ".cr2", ".arw", ".svg", ".ico"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx", ".htm", ".html", ".md", ".epub", ".xml", ".json", ".log", ".mobi"],
            "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".3gp", ".mpeg", ".mpg", ".ogv", ".m4v", ".divx"],
            "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".amr", ".opus", ".ape"],
            "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".lzh", ".cab", ".z", ".ace"]
        }
        
        for folder_name, exts in extensions.items():
            folder_dir = os.path.join(self.folder_path, folder_name)
            if not os.path.exists(folder_dir):
                os.makedirs(folder_dir)
                
            for file_name in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file_name)
                if os.path.isfile(file_path):
                    if any(file_name.lower().endswith(ext) for ext in exts):
                        shutil.move(file_path, folder_dir)
        
        messagebox.showinfo("Success", "The Directory Organized!")
        self.selected_folder_label.config(text="Selected Directory: None")
        self.folder_path = ""
        
    def list_folder_contents(self):
        if not self.folder_path:
            messagebox.showerror("Select", "Please, select directory!")
            return
        
        # Clear text area.
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)
        
        # List the inside of directory.
        def list_dir_contents(folder, level=0):
            items = os.listdir(folder)
            for item in items:
                item_path = os.path.join(folder, item)
                if os.path.isdir(item_path):
                    self.text_area.insert(tk.END, f"{'|   ' * level}--- {item}\n")
                    list_dir_contents(item_path, level + 1)
                else:
                    self.text_area.insert(tk.END, f"{'|   ' * level}    --- {item}\n")
        
        self.text_area.insert(tk.END, f"{self.folder_path}\n")
        self.text_area.insert(tk.END, "|\n")
        list_dir_contents(self.folder_path)
        
        # Disabled the text area.
        self.text_area.config(state="disabled")

# Run the app.
if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()