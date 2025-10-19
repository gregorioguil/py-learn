from fastapi import APIRouter, HTTPException, status, Body
from models.user import UserCreate, UserLogin
from db.users import create_user, get_user_by_username

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate = Body(...)):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    new_user = create_user(user.username, user.password)
    return {"id": new_user["id"], "username": new_user["username"]}

@router.post("/login")
def login(user: UserLogin = Body(...)):
    db_user = get_user_by_username(user.username)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    return {"id": db_user["id"], "username": db_user["username"]}
