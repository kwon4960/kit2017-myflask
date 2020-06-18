
from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json
import dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello/')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)
    
@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['items'])
    return  "{} 이 {} 아이템을 사용 해서 이겼다".format(character["name"], character["items"][0])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"
    else:
        return "없어요"
        
@app.route('/')
def hello():
    return '아이디 또는 패스워드를 확인 하세요.' 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
       
        if id == 'abc' and pw == '1234':
            return '''
                <script> alert("안녕하세요~ {}님");
                location.href="/form"
                </script>
            '''.format (id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))

@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        return 'GET 으로 전송이다.' 
    else: num = request.form["num"]
        name = request.form["name"]
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)
if __name__ == '__main__': 
    app.run(debug=True)

