from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Главная страница"}


@app.get("/users/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/users/{id}")
async def user(id: int):
    return {"message": f"Вы вошли как пользователь {id}"}


@app.get("/users")
async def users(user: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {user}, Возраст: {age}"}
