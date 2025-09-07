# project-day-8
# File Sorter by Date

A **Python script** that organizes files into **Today, This_Week, and Older** folders based on their last modified date.  
This project helps keep directories like Downloads clutter-free with a simple and efficient automation tool.

---

## Features

-  Automatically creates Today, This_Week, and Older folders  
-  Sorts files by last modified date  
-  GUI folder picker (no need to edit paths manually)  
-  Works on Windows, Mac, and Linux  
-  Beginner-friendly and lightweight  

---

## Technologies Used

- **Python 3** – Core programming language  
- **os** – File and directory handling  
- **shutil** – Moving files between folders  
- **datetime** – Date comparison for sorting  
- **tkinter** – Folder selection GUI  

---

## Project Structure

file-sorter/
│── filesort.py   # Main Python script  
│── README.md     # Documentation  

---

## How to Run

1. Clone the repository.  
2. Run the script:  
   ```bash
   python filesort.py
Select the folder you want to organize when the GUI window appears.

Files will be moved into Today, This_Week, and Older automatically.


mathematica
Copy code
Downloads/
   ├── Today/
   │   └── report.pdf
   ├── This_Week/
   │   └── song.mp3
   └── Older/
       └── old_photo.jpg
Author
Swara Gharat
