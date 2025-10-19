from fastapi import APIRouter, Query
from quiz_database import (
    get_quiz_questions,
    get_question_by_id,
    get_quiz_topics,
    get_quiz_difficulties
)

router = APIRouter()

@router.get("/quiz")
def get_quiz(
    limit: int = Query(20, description="Limite de perguntas"),
    topic: str = Query(None, description="Filtrar por tópico"),
    difficulty: str = Query(None, description="Filtrar por dificuldade")
):
    questions = get_quiz_questions(limit=limit, topic=topic, difficulty=difficulty)
    return questions

@router.get("/quiz/{question_id}")
def get_quiz_question(question_id: int):
    question = get_question_by_id(question_id)
    if not question:
        return {"error": "Pergunta não encontrada"}
    return question

@router.get("/quiz-topics")
def get_quiz_topics_endpoint():
    return get_quiz_topics()

@router.get("/quiz-difficulties")
def get_quiz_difficulties_endpoint():
    return get_quiz_difficulties()
