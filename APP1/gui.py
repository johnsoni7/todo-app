import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do: ")
input = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [input, add_button]])
window.read()
window.close()