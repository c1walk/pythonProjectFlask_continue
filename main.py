from flask import Flask

app = Flask(__name__)

@app.route('/')
def page_index():
    return "Не главная страничка"

@app.route('/feed')
def page_feed():
    return "Лента пльзователя"

app.run(host='127.0.0.2', port=80)