from flask import Flask, render_template
import random

app = Flask(__name__)

heros = ['张无忌', '张三丰', '令狐冲', '郭靖', '杨过', '一灯大师']


@app.route('/')
def index():
    return render_template('index.html', heros=heros)


@app.route('/choujiang')
def choujiang():
    num = random.randint(0, len(heros) - 1)
    return render_template('index.html', num=num, heros=heros)


app.run(debug=True)
