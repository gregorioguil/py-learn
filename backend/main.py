from progress_database import save_user_progress, get_user_progress
# --- PROGRESSO DO USUÁRIO ---
from fastapi import Body

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, progress, exercises, quiz
from user_models import UserCreate, UserLogin
from users_database import create_user, get_user_by_username
from fastapi import Body
from progress_database import save_user_progress, get_user_progress
from exercises_database import (
    get_all_exercises, 
    get_exercise_by_id, 
    get_exercises_by_topic, 
    get_exercises_by_difficulty
)
from quiz_database import (
    get_quiz_questions,
    get_question_by_id,
    get_quiz_topics,
    get_quiz_difficulties
)

app = FastAPI()

# Configuração CORS correta para frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique ["http://localhost:3000"] se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(progress.router)
app.include_router(exercises.router)
app.include_router(quiz.router)
@app.post("/register", status_code=201)
def register(user: UserCreate = Body(...)):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    new_user = create_user(user.username, user.password)
    return {"id": new_user["id"], "username": new_user["username"]}
    #return {"error": "Tópico não encontrado"}
    #return exercises

@app.get("/exercises/difficulty/{difficulty}")
def get_exercises_by_difficulty_endpoint(difficulty: str):
    """Retorna exercícios de uma dificuldade específica"""
    exercises = get_exercises_by_difficulty(difficulty)
    return exercises

@app.get("/topics")
def get_topics():
    """Retorna todos os tópicos disponíveis"""
    topics = {
        "basic": "Princípios Básicos",
        "conditionals": "Estruturas Condicionais", 
        "loops": "Loops",
        "lists": "Listas",
        "dictionaries": "Dicionários",
        "functions": "Funções",
        "advanced_data_structures": "Estruturas de Dados Avançadas",
        "algorithms": "Algoritmos Básicos"
    }
    return topics

@app.get("/quiz")
def get_quiz(
    limit: int = Query(20, description="Limite de perguntas"),
    topic: str = Query(None, description="Filtrar por tópico"),
    difficulty: str = Query(None, description="Filtrar por dificuldade")
):
    """Retorna perguntas do quiz com filtros opcionais"""
    questions = get_quiz_questions(limit=limit, topic=topic, difficulty=difficulty)
    return questions

@app.get("/quiz/{question_id}")
def get_quiz_question(question_id: int):
    """Retorna uma pergunta específica do quiz por ID"""
    question = get_question_by_id(question_id)
    if not question:
        return {"error": "Pergunta não encontrada"}
    return question

@app.get("/quiz-topics")
def get_quiz_topics_endpoint():
    """Retorna todos os tópicos de quiz disponíveis"""
    return get_quiz_topics()

@app.get("/quiz-difficulties")
def get_quiz_difficulties_endpoint():
    """Retorna todos os níveis de dificuldade de quiz"""
    return get_quiz_difficulties()

@app.get("/progress")
def get_progress():
    return {"lessons_completed": 1, "exercises_completed": 0, "quiz_score": 0}