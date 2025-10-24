from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Главная — теперь рендерит шаблон с ссылками
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h2>О проекте</h2><p>Разработчик: Эммануэль Рох<br>Цель: демонстрация Flask-приложения с 4 страницами.</p>"

@app.route('/data')
def data():
    info = {
        "project": "Flask Demo App",
        "author": "Emmanuel Rokh",
        "version": "1.0",
        "language": "Python"
    }
    return jsonify(info)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"<h3>Привет, {name}!</h3><p>Данные успешно отправлены.</p>"

    html_form = '''
        <h2>Добавить данные</h2>
        <form method="post">
            <input name="name" placeholder="Введите имя">
            <button type="submit">Отправить</button>
        </form>
    '''
    return html_form

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
