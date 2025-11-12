from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Приложение успешно развернуто на Vercel!"}

@app.get("/about")
def about():
    return {"info": "Это тестовый API на FastAPI"}
