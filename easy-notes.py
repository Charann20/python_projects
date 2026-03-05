import tkinter as tk
from tkinter import messagebox

# function to save note
def save_note():
    note = text_area.get("1.0", tk.END)
    
    if note.strip() == "":
        messagebox.showwarning("Warning", "Note is empty!")
    else:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        messagebox.showinfo("Saved", "Note saved successfully!")
        text_area.delete("1.0", tk.END)

# function to clear note
def clear_note():
    text_area.delete("1.0", tk.END)

# main window
root = tk.Tk()
root.title("Simple Notes App")
root.geometry("400x400")

# title label
label = tk.Label(root, text="My Notes", font=("Arial", 16))
label.pack(pady=10)

# text area
text_area = tk.Text(root, height=15, width=40)
text_area.pack(pady=10)

# buttons
save_btn = tk.Button(root, text="Save Note", command=save_note)
save_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear_note)
clear_btn.pack(pady=5)

# run app
root.mainloop()
