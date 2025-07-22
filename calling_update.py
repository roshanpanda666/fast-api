import requests
todo_id = "687f4d28900c166e834d9995"  # Replace with actual ID
updated_todo = {
    "title": "Updated Title ✨",
    "description": "Updated description",
    "complete": True
}

response = requests.put(f"http://127.0.0.1:8000/{todo_id}", json=updated_todo)
print(response.json())
