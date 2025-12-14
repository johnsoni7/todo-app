**📝 To-Do App (Python: GUI + CLI + Web App)**

**🌐 Live Web App**

👉 https://johns-todo-app.streamlit.app/

A complete To-Do application built in Python with three different interfaces:

🖥 GUI App – Built using FreeSimpleGUI

💻 CLI App – Terminal-based todo manager

🌐 Web App – Built using Streamlit

All three versions share the same backend file handler: functions.py

**🚀 Features**

**✅ GUI Version (FreeSimpleGUI)**

1. Add new todos

2. Edit existing todos

3. Mark todos as complete

4. Auto-creates todos.txt if missing

5. Buttons with PNG icons (add.png, complete.png)

6. Live updating digital clock

7. Popup warnings when no todo is selected

8. Real-time list refresh

**🖥 CLI Version**

1. Add todos

2. Show all todos

3. Edit todos

4. Complete/remove todos

5. Handles invalid inputs gracefully

6. Simple and lightweight

**🌐 Web App Version (Streamlit)**

1. Beautiful and interactive UI

2. dd todos via text input

3. Edit or delete existing todos

4. Instant updates using st.session_state

5. Runs entirely in the browser

6. Perfect for online deployment (Streamlit Cloud)

**📂 Project Structure**
.
├── gui.py            # Desktop GUI App (FreeSimpleGUI)
├── cli.py            # Command-Line App
├── web.py            # Streamlit Web App
├── functions.py      # Shared read/write logic for todos.txt
├── todos.txt         # Todo storage file
├── add.png           # Add button icon
├── complete.png      # Complete button icon
└── README.md         # Documentation

**🧠 How It Works**

All todo items are stored inside todos.txt.

functions.py provides two helper functions:
def get_todo(filename="todos.txt"):
    # Reads todos from file

def write_todo(todos, filename="todos.txt"):
    # Writes todos back to file


All three app versions rely on these functions for consistent behavior.

**📌 Requirements**

Install dependencies:

pip install FreeSimpleGUI streamlit

▶️ Run the Apps
GUI App
python gui.py

CLI App
python cli.py

Web App (Streamlit)
streamlit run web.py


This launches the app in your browser at:

http://localhost:8501

🌐 Deploying the Web App Online

You can deploy web.py using Streamlit Cloud:

Push your repository to GitHub

Visit: https://streamlit.io/deploy

Select your repo

Set main file to web.py

Deploy 🚀

✨ Author

John Soni Thomas