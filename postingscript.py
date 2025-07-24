# posting new data
import asyncio
from routes.route import create_todo
import requests
from models.todos import Todo

response=requests.get("https://fast-api-1-uh0r.onrender.com/latest")
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
    "complete":input("completed ?: "),

}

#call the fast api function

result=asyncio.run(create_todo(new_todo_data))
print(result)


print("new data -- \n",f"Title: {todo.title}\nDone: {todo.complete} \ndescription: {todo.description}")
