import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do: ")
input = sg.InputText(tooltip="Enter To-Do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", 
                   layout=[[label], [input, add_button]], 
                   font=('Helvetica', 15))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todos = value['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()