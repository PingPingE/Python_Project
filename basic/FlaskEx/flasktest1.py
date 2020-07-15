from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/method/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

# @app.route('/login')
# def login1():
#     user = request.args.get('name') #Get 방식: /login?name=이름
#     return 'User %s'%user

@app.route('/login', methods=['POST'])
def login2():
    #request.form은 딕셔너리 형태
    username = request.form['username']
    pw = request.form['pw']
    return f"username:{username} pw:{pw}"

@app.route('/login')
def login3():
    username = request.args.get('username')
    pw = request.args.get('pw')
    return f"username:{username} pw:{pw}"


if __name__ == '__main__':
    app.run(debug=True,port=8011)