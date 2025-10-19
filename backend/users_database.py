# Simple in-memory user store for demonstration (replace with DB in production)
users_db = []

def create_user(username: str, password: str):
    user_id = len(users_db) + 1
    user = {"id": user_id, "username": username, "password": password}
    users_db.append(user)
    return user

def get_user_by_username(username: str):
    for user in users_db:
        if user["username"] == username:
            return user
    return None
