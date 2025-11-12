from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Приложение успешно работает на Vercel!"
