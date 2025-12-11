def get_todo(filename = 'todos.txt'):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_todo(todos, filename = 'todos.txt'):
    with open(filename, 'w') as file:
        file.writelines(todos)


#for every python file, that file itself is the main.py
# print(__name__)
if __name__ == '__main__':
    print("Hello")