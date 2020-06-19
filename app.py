
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
        print (id,type(id))
        print (pw,type(pw))  
        ret = dbdb.select_user(id, pw) 
        print(ret)
        if ret != None:
            return "안녕하세요~ {} 님".format(ret[2])
        else:    
            return "아이디 또는 패스 워드를 확인 하세요."

# 회원 가입 
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        print (id,type(id))
        print (pw,type(pw))
        ret = dbdb.check_id(id)
        if ret != None:
            return '''
                    <script>
                    alert('다른 아이디를 사용하세요');
                    location.href='/join';
                    </script>
                    '''
                    
        dbdb.select_user(id, pw, name) 
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
    if id == 'abc' and pw == '1234'
        session['user'] = id
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)  

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret[3])
    return render_template('getinfo.html', data=ret)
    # return '번호 : {}, 이름 : {}'.format(student[0], student[1])
    
@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")

@app.route('/img')
def img():
    return render_template("image.html")

if __name__ == '__main__':
    app.run(debug=True)
 
