# 🗂️ File Organizer – CLI Tool

A terminal-based file organizer that helps users clean up messy folders by sorting files either by **file type** or **modification date**. Built with Python and designed for real-world productivity needs.

---

## 🚀 Features

- ✅ Organize files by **Type** (e.g., PDFs, JPGs, TXTs, DOCXs)
- ✅ Organize files by **Date** (based on last modified date)
- ✅ Choose to **Move** files into folders or **Rename** them with prefixes
- ✅ Clear instructions and feedback directly in the terminal
- ✅ Includes color-enhanced output using `colorama`

---

## 🖼️ Sample Output

A sample run showing organization by file type in the terminal:

![File Organizer Screenshot](https://raw.githubusercontent.com/Ek-Coder-Tech/file-organizer-cli/main/file_organizer.png)

---

## 📂 How It Works

1. User is prompted to enter the name of the folder to organize (must exist in the current directory).
2. User chooses how to organize files:  
   - `'type'`: by file extensions (e.g., `.pdf`, `.jpg`, `.txt`)  
   - `'date'`: by file modification dates (e.g., `2024-10-01`)
3. User selects whether to:  
   - `'move'` files into folders, or  
   - `'rename'` files using a prefix
4. Script scans the folder, applies changes, and prints a summary of the results.

---

## 🔧 Technologies Used

- **Python 3.x**
- Built-in modules: `os`, `shutil`, `datetime`
- `colorama` for enhanced terminal output (cross-platform)

---

## 💼 Use Cases

Organizing downloaded files by month or type

Preparing files for upload or backup

Renaming photos, documents, or scanned files

Lightweight alternative to complex file management tools

---

## 🔍 Folder Structure

bash

Copy

Edit

file-organizer-cli/

├── main.py            # Python script

├── file_organizer.png     # Terminal + code screenshot

├── README.md          # Project documentation

└── test_folder/       # (Optional) Sample folder for demo

---

## 🙌 Author

**Eric Mutisya**  
Python Developer | Web Developer | Freelancer  
Upwork Profile: https://www.upwork.com/freelancers/~012558bab6232e8e65

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project with attribution.

---

## 🙋‍♂️ Author's Note

This project was built as part of my practical journey into freelance development using Python.  
If you're a client looking for a similar automation or document solution — I'd be happy to help!  
Let’s connect on [Upwork](https://www.upwork.com/freelancers/~012558bab6232e8e65) or [GitHub](https://github.com/Ek-Coder-Tech).
