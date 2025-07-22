#getting the latest data

import requests
from models.todos import Todo

response = requests.get("http://127.0.0.1:8000/latest")
todo_data = response.json()

# Convert single dict to Todo object
todo = Todo(**{

    "title": todo_data["title"],
    "description": todo_data["description"],
    "complete": todo_data["complete"]
})


print(f"Title: {todo.title}\nDone: {todo.complete} \ndescription: {todo.description}")
