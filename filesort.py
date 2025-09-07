import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog

def sort_files_by_date(folder_path):
    today = datetime.date.today()
    
    today_folder = os.path.join(folder_path, "Today")
    week_folder = os.path.join(folder_path, "This_Week")
    older_folder = os.path.join(folder_path, "Older")

    for f in [today_folder, week_folder, older_folder]:
        if not os.path.exists(f):
            os.makedirs(f)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            continue

        mtime = os.path.getmtime(file_path)
        file_date = datetime.date.fromtimestamp(mtime)

        if file_date == today:
            dest = today_folder
        elif (today - file_date).days <= 7:
            dest = week_folder
        else:
            dest = older_folder

        shutil.move(file_path, os.path.join(dest, file))
        print(f"Moved: {file} → {dest}")

root = tk.Tk()
root.withdraw()
folder = filedialog.askdirectory(title="Select a folder to sort")

if folder:
    sort_files_by_date(folder)
    print("\n✅ Sorting complete!")
else:
    print("\n❌ No folder selected. Exiting...")
