from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field
from typing import List


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=20, description='Username')
    age: int = Field(..., ge=18, le=120, description='User age')


app = FastAPI()

users = []


@app.get('/users', response_model=List[User])
async def get_all_users() -> list:
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def register_user(username: str, age: int) -> User:
    if len(users):
        user_id = users[-1].id + 1
    else:
        user_id = 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: int) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return user
    raise HTTPException(status_code=404, detail="User was not found")
