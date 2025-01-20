from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Главная страница"}


@app.get("/users/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/users/{id}")
async def user(id: int = Path(ge=0, le=100, description='ID пользователя')):
    return {"message": f"Вы вошли как пользователь {id}"}


@app.get("/user/{user}/{age}")
async def users(user: str = Path(min_length=5, max_length=10, description='Enter username'),
                age: int = Path(ge=18, le=120, description='Enter age')):
    return {"message": f"Информация о пользователе. Имя: {user}, Возраст: {age}"}
