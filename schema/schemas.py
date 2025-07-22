def individual_serial(todo)->dict:
    return{
        "id":str(todo["_id"]),
        "title":str(todo["title"]),
        "description":str(todo["description"]),
        "complete":str(todo["complete"])
    }

def list_serial(todos)->list:
    return[individual_serial(todo) for todo in todos]