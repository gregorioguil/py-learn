# Simples banco de dados em memória para progresso do usuário
user_progress_db = {}

def save_user_progress(username, progress):
    user_progress_db[username] = progress
    return progress

def get_user_progress(username):
    return user_progress_db.get(username, {
        "xp": 0,
        "streak": 1,
        "badges": [],
        "phases": []
    })
