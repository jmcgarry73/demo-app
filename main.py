import os
import sys
import tempfile
import webbrowser
from pathlib import Path

import requests
import tkinter as tk
from tkinter import messagebox

from version import APP_NAME, APP_VERSION

GITHUB_USER = "jmcgarry73"
GITHUB_REPO = "demo-app"

LATEST_RELEASE_URL = (
    f"https://api.github.com/repos/"
    f"{GITHUB_USER}/{GITHUB_REPO}/releases/latest"
)

def resource_path(relative_path):
    """
    Get absolute path to resource,
    works for dev and PyInstaller.
    """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def check_updates():
    try:
        response = requests.get(LATEST_RELEASE_URL, timeout=5)
        response.raise_for_status()

        latest_release = response.json()

        latest_version = latest_release["tag_name"].lstrip("v")

        if latest_version != APP_VERSION:

            assets = latest_release.get("assets", [])

            installer_url = None

            for asset in assets:
                name = asset["name"]

                if name.endswith(".exe"):
                    installer_url = asset["browser_download_url"]
                    break

            if installer_url is None:
                messagebox.showerror(
                    "Update Error",
                    "No installer found in release."
                )
                return

            result = messagebox.askyesno(
                "Update Available",
                (
                    f"Version {latest_version} is available.\n\n"
                    f"Would you like to download it?"
                )
            )

            if result:
                webbrowser.open(installer_url)

        else:
            messagebox.showinfo(
                "Updates",
                "You are running the latest version."
            )

    except Exception as e:
        messagebox.showerror(
            "Update Error",
            str(e)
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

root.iconbitmap(resource_path("assets/icon.ico"))

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