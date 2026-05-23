import tkinter as tk
from tkinter import messagebox

APP_NAME = "Demo App"
APP_VERSION = "1.0.0"


def check_updates():
    messagebox.showinfo(
        "Updates",
        "You are running the latest version."
    )


def show_about():
    messagebox.showinfo(
        "About",
        f"{APP_NAME}\nVersion {APP_VERSION}"
    )


root = tk.Tk()
root.title(APP_NAME)
root.geometry("500x300")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text=APP_NAME,
    font=("Segoe UI", 20)
)
title_label.pack(pady=(40, 10))

version_label = tk.Label(
    root,
    text=f"Version {APP_VERSION}",
    font=("Segoe UI", 10)
)
version_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=30)

update_button = tk.Button(
    button_frame,
    text="Check for Updates",
    width=20,
    command=check_updates
)
update_button.grid(row=0, column=0, padx=10)

about_button = tk.Button(
    button_frame,
    text="About",
    width=20,
    command=show_about
)
about_button.grid(row=0, column=1, padx=10)

root.mainloop()