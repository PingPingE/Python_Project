from flask import Flask, render_template

app = Flask(__name__)

#요청에대해 처리할 것
#controller에 적은 주소값같은 것
@app.route('/')
def index():
    return render_template('index.html') #templates폴더 안에 있는 파일을 불러옴

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

#post방식, ?형태는 함수 매개변수에 선언X 하지만 아래와 같은 경우는 매개변수 필요 
@app.route('/user/<username>') #<int:age> 처럼 자료형 지정도 가능
def show_user_profile(username): #매개변수 이름은 위 변수 이름이랑 똑같아야함
    return f'User {username}'

#실행할 내용
if __name__ == '__main__':
    app.run(debug=True, port=8089)


