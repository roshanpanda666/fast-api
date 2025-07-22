import requests

todo_id = "687f4d28900c166e834d9995"  # Replace with actual ID

response = requests.delete(f"http://127.0.0.1:8000/{todo_id}")
print(response.json())