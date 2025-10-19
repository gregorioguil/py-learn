from fastapi import APIRouter, Query
from exercises_database import (
    get_all_exercises, 
    get_exercise_by_id, 
    get_exercises_by_topic, 
    get_exercises_by_difficulty
)

router = APIRouter()

@router.get("/exercises")
def get_exercises(
    topic: str = Query(None, description="Filtrar por tópico"),
    difficulty: str = Query(None, description="Filtrar por dificuldade"),
    limit: int = Query(50, description="Limite de exercícios")
):
    exercises = get_all_exercises()
    if topic:
        exercises = [ex for ex in exercises if ex.get('topic') == topic]
    if difficulty:
        exercises = [ex for ex in exercises if ex.get('difficulty') == difficulty]
    return exercises[:limit]

@router.get("/exercises/{exercise_id}")
def get_exercise(exercise_id: int):
    exercise = get_exercise_by_id(exercise_id)
    if not exercise:
        return {"error": "Exercício não encontrado"}
    return exercise

@router.get("/exercises/topic/{topic}")
def get_exercises_by_topic_endpoint(topic: str):
    exercises = get_exercises_by_topic(topic)
    if not exercises:
        return {"error": "Tópico não encontrado"}
    return exercises

@router.get("/exercises/difficulty/{difficulty}")
def get_exercises_by_difficulty_endpoint(difficulty: str):
    exercises = get_exercises_by_difficulty(difficulty)
    return exercises
