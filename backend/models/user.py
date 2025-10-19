from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
