import os
import json
import customtkinter as ctk
from tkinter import filedialog, scrolledtext, messagebox

# Set CustomTkinter theme
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

def folder_to_json(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError("Invalid folder path, please check the input.")
    
    name = os.path.basename(path) or os.path.abspath(path)
    tree = {'name': name, 'type': 'directory', 'children': []}
    
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            tree['children'].append(folder_to_json(item_path))
        else:
            tree['children'].append({'name': item, 'type': 'file'})
    
    return tree

class FolderJSONApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Folder Structure to JSON")
        self.geometry("600x500")
        
        # Path input
        self.path_label = ctk.CTkLabel(self, text="Folder Path:")
        self.path_label.pack(pady=10)
        
        self.path_entry = ctk.CTkEntry(self, width=400)
        self.path_entry.pack(pady=5)
        
        # Browse folder button
        self.browse_button = ctk.CTkButton(self, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(pady=5)
        
        # Generate JSON button
        self.generate_button = ctk.CTkButton(self, text="Generate JSON", command=self.generate_json)
        self.generate_button.pack(pady=10)
        
        # JSON display area (using ScrolledText for scrolling)
        self.json_text = scrolledtext.ScrolledText(self, width=70, height=15, wrap="word")
        self.json_text.pack(pady=10)
        
        # Save JSON button
        self.save_button = ctk.CTkButton(self, text="Save JSON to File", command=self.save_json)
        self.save_button.pack(pady=5)
        
        self.json_data = None  # Store generated JSON data
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_entry.delete(0, ctk.END)
            self.path_entry.insert(0, folder_path)
    
    def generate_json(self):
        path = self.path_entry.get()
        if not path:
            messagebox.showerror("Error", "Please enter or select a folder path!")
            return
        
        try:
            self.json_data = folder_to_json(path)
            json_str = json.dumps(self.json_data, indent=4, ensure_ascii=False)
            self.json_text.delete(1.0, ctk.END)
            self.json_text.insert(ctk.END, json_str)
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def save_json(self):
        if not self.json_data:
            messagebox.showwarning("Warning", "Please generate JSON first!")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.json_data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Success", "JSON has been saved!")

# Run the application
if __name__ == "__main__":
    app = FolderJSONApp()
    app.mainloop()