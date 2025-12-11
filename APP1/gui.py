import functions
import FreeSimpleGUI as sg
import time

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do: ")

input = sg.InputText(tooltip="Enter To-Do", key="todo")

add_button = sg.Button(size=2, image_source="add.png", button_color=("white"), tooltip="Add Todo", key="Add")

list_box = sg.Listbox(values=functions.get_todo(), key='todos', 
                      enable_events=True, size=[45,10]) 

#List box can show 45 characters wide and 10 rows before scrolling needed
#If the user clicked an item in the Listbox, then: 
# event will be "todos" ← (the key of the Listbox) 
# values["todos"] will contain the selected item(s)

edit_button = sg.Button("Edit")

complete_todo = sg.Button(key="Complete", size=2, image_source="complete.png", tooltip="complete-todo")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App", 
                   layout=[[clock],[label], [input, add_button],[list_box,edit_button,complete_todo], [exit_button]], 
                   font=('Helvetica', 15))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value = time.strftime("%b %d,%Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todos = value['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todo(todos)
            window['todos'].update(values=todos) 

        case 'Edit':
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo'] + '\n'

                todos = functions.get_todo()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an item first", font=("Helvetica", 15))

        case 'todos':
            window['todo'].update(value=value['todos'][0])
            
        case 'Complete':
            try:
                completed_todo = value['todos'][0] 
                todos = functions.get_todo() 
                todos.remove(completed_todo) 
                functions.write_todo(todos) 
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an item first", font=("Helvetica", 15))
        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

window.close()