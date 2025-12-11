import functions
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is ", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]+ "\n"

        todos = functions.get_todo()

        todos.append(todo)

        functions.write_todo(todos)


    elif user_action.startswith('show'):

        todos = functions.get_todo()

        for index, todo in enumerate(todos):
            print(f"{index+1}. {todo.strip()}")
                

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todo()

            index = int(user_action[5:]) - 1

            new_todo = input("Enter new todo: ") + "\n"
            todos[index] = new_todo

            functions.write_todo(todos)

        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no item with that number")

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todo()

            index = int(user_action[9:]) - 1

            todo_to_remove = todos[index]
            todos.pop(index)

            print(f"{todo_to_remove.strip()} was removed from the list")

            functions.write_todo(todos)
            
        except ValueError:
            print("Your command is not valid")
        except IndexError:
            print("There is no item with that number")
            

    elif user_action.startswith('exit'): 
        break

    else:
        print("Command not valid. Try again!")
print("BYE!")