from fastapi import APIRouter, Body
from db.progress import save_user_progress, get_user_progress

router = APIRouter()

@router.post("/progress/{username}")
def save_progress(username: str, progress: dict = Body(...)):
    return save_user_progress(username, progress)

@router.get("/progress/{username}")
def get_progress_user(username: str):
    return get_user_progress(username)
