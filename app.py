import random

def game(num, character ):

    if num == 1:

        print("1. 공격 2. 아이템 사용.")

        num = int(input("선택: "))

        if num ==1:

             print(random.choice(character["skill"]))

             print("강도 제압후 경찰에 넘기다.")

        elif num == 2:

            print(random.choice(character["items"]))

            print("강도 기절후 경찰에 넘기다.")

    elif num == 2:  

        print("도망가다 강도에게 맞아서 HP 0")

    else:

        print("입력 잘못 해서 게임 끝.")

 

def charact(name):

    character = {

        "name": name,

        "level": 1,

        "hp": 100,

        "items": ["전기충격기", "야구방망이", "휴대폰"],

        "skill": ["이단돌려차기", "니킥", "뒤돌려차기"]

    }

    print("{0}님 반갑습니다. (HP {1})으로 게임을 시작 합니다.".format(character["name"], character["hp"]))

    return character

 

def save_game(filename, charact):

    f = open(filename, "w", encoding="utf-8")

    for key in character:

        print("%s:%s" % (key, character[key]))

        f.write("%s:%s\n" % (key, character[key]))

    f.close()

 

name = input("이름을 입력하시오: ")

 

character = charact(name)

 

 

save_game("save.txt", character)

 

 

print("길을 가다가 강도를 만났습니다.")

while(True):

    try:

        print("1. 싸운다 2. 도망간다")

        num = int(input("선택: "))

        break

    except:

        print("숫자만 입력.")

game(num, character)

















from flask import Flask, request, render_template
app = Flask(__name__)

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
            return "안녕하세요~ {} 님".format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)  
         


@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")

@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/urltest')
def url_test():
    return redirect(url_for('naver'))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))

if __name__ == '__main__':
    app.run(debug=True)