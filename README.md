# 📂 File Organizer (Python CLI Tool with Colorama)

A simple, colorful command-line tool built with Python that helps you organize files in a folder by **file type** or **modification date**. Ideal for individuals or small teams who want a lightweight automation tool without complicated setup.

---

## 🔧 Features

- 🗂️ Organize files by **type** (e.g., PDF, JPG, TXT)
- 📅 Organize files by **last modified date** (e.g., 2025-07)
- 🎨 Uses **Colorama** to highlight key actions and feedback
- 🛠️ Choose between:
  - **Move** files into folders
  - **Rename** files with type or date prefixes
- 🧑‍💻 Easy to use in the terminal — no external tools required

---

## 🖥️ How It Works

1. Run the script in a terminal or IDE (like Replit or VS Code)
2. Enter the name of the folder containing your files (e.g., `test_folder`)
3. Choose whether to organize by:
   - `type` → groups files by extension
   - `date` → groups files by last modified date
4. Choose whether to:
   - `move` → place files into subfolders
   - `rename` → prefix file names instead of moving

---

## 📁 Example Output

```bash
📂 Welcome to File Organizer!
📁 Enter the folder name to organize: test_folder
🔎 Looking in folder: /home/runner/workspace/test_folder
🔧 Choose organization method ('type' or 'date'): type
🛠️  Do you want to 'move' files into folders or just 'rename' them? rename
✅ 4 file(s) renamed with type prefix.

## 🖥️ Sample Output
A sample run of the script showing how files are organized by type using the terminal.
![File Organizer Screenshot](https://raw.githubusercontent.com/Ek-Coder-Tech/file-organizer-cli/main/File_Organizer.png)

💼 Use Cases
Organizing downloaded files by month or type

Preparing files for upload or backup

Renaming photos, documents, or scanned files

Lightweight alternative to complex file management tools

🧑‍💻 Technologies Used
Python 3

Colorama (for terminal color)

Built-in modules: os, shutil, datetime

🚀 Getting Started
Requirements
Python 3.x

colorama package

Installation (Local)
bash
Copy
Edit
pip install colorama
Run the Script
bash
Copy
Edit
python main.py
🔍 Folder Structure
bash
Copy
Edit
file-organizer-python-cli/
│
├── main.py            # Python script
├── screenshot.png     # Terminal + code screenshot
├── README.md          # Project documentation
└── test_folder/       # (Optional) Sample folder for demo

🧑‍🎓 Author
Eric Mutisya
Freelance Python Developer
GitHub: Ek-Coder-Tech

📜 License
This project is open-source and free to use.
Attribution appreciated but not required.

🙌 Acknowledgements
Thanks to Colorama for bringing life to the terminal — and to all open-source contributors who help beginners build real tools!
