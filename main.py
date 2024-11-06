import tkinter as tk
from tkinter import filedialog, messagebox

class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Code Editor")
        self.file_path = None

        # Create a Text widget for the code editor
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        # Add a menu bar with 'File' options
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Create a status bar to show the file name
        self.status_bar = tk.Label(root, text="No file opened", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

    def open_file(self):
        # Prompt the user to select a file to open
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.file_path = file_path
                self.update_status_bar()
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open file: {e}")

    def save_file(self):
        # Save the current content to the opened file or prompt for a save location if no file is opened
        if self.file_path:
            self._write_to_file(self.file_path)
        else:
            self.save_as_file()

    def save_as_file(self):
        # Prompt the user to choose a file name and location to save the current content
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            self._write_to_file(file_path)
            self.file_path = file_path
            self.update_status_bar()

    def _write_to_file(self, file_path):
        # Write the current content to the specified file
        try:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            messagebox.showinfo("Success", f"File saved to: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to save file: {e}")

    def update_status_bar(self):
        # Update the status bar with the current file name
        self.status_bar.config(text=self.file_path if self.file_path else "No file opened")

# Initialize and run the application
root = tk.Tk()
editor = CodeEditor(root)
root.mainloop()
