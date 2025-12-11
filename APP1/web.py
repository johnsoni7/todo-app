import streamlit as st
import functions

todos = functions.get_todo()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todo(todos)



st.title('My To-Do App')
st.subheader('This is my To-do app')
st.write("This app is to increase your productivity.")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

# st.session_state
