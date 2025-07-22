import asyncio
from routes.route import create_todo
import requests
from models.todos import Todo

response=requests.get("http://127.0.0.1:8000/latest")
todo_data=response.json()

# Convert single dict to Todo object
todo = Todo(**{

    "title": todo_data["title"],
    "description": todo_data["description"],
    "complete": todo_data["complete"]
})

new_todo_data={
    "title":input("title: "),
    "description":input("description: "),
    "complete":input("completed ? type True/False: "),

}

#call the fast api function

result=asyncio.run(create_todo(new_todo_data))
print(result)


print("new data -- \n",f"Title: {todo.title}\nDone: {todo.complete} \ndescription: {todo.description}")
