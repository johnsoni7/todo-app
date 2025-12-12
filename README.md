# 📝 To-Do App (Python + FreeSimpleGUI)

A simple and functional To-Do application built using **Python**, **FreeSimpleGUI**, and **file-based storage**.  
This project includes **two versions** of the app:

1. **GUI Version** – A desktop application using FreeSimpleGUI  
2. **CLI Version** – A command-line based todo manager  

Both versions use the same backend `functions.py` for reading/writing todos.

---

## 🚀 Features

### ✅ GUI Version
- Add new todos  
- Edit existing todos  
- Mark todos as complete (delete)  
- Live clock display  
- Automatically creates `todos.txt` if missing  
- Buttons with icons (`add.png`, `complete.png`)  
- Error popups when no todo is selected  
- Smooth real-time updates

### 🖥 CLI Version
- Add todos  
- Show all todos  
- Edit todos  
- Complete (remove) todos  
- Input-based navigation  
- Error handling for invalid commands  

---

## 📂 Project Structure
.
├── gui.py # GUI Application
├── cli.py # CLI Application
├── functions.py # File read/write logic
├── todos.txt # Todo storage file
├── add.png # Add button icon
├── complete.png # Complete button icon
└── README.md


## 🧠 How It Works

All todos are stored in **`todos.txt`**.  
The helper functions:

1. def get_todo()
2. def write_todo()

**📌 Requirements**

Python 3.x

FreeSimpleGUI

**Install FreeSimpleGUI:**
pip install FreeSimpleGUI

**▶️ Running the GUI App**
python gui.py

**▶️ Running the CLI App**
python cli.py


✨ Author
John Soni Thomas
