FILEPATH = "todos.txt"
def get_todo(filename = FILEPATH):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_todo(todos, filename = FILEPATH):
    with open(filename, 'w') as file:
        file.writelines(todos)


#for every python file, that file itself is the main.py
# print(__name__)
if __name__ == '__main__':
    print("Hello")