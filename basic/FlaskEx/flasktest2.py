from flask import Flask, render_template,request
app = Flask(__name__)
users = []

@app.route('/')
def index():
    return render_template('form_input.html')

@app.route('/login', methods= ['post'])
def login():
    result = request.form
    users.append(result)
    print(users)
    return render_template('form_result.html', result = users)

if __name__ == "__main__":
    app.run(debug= True, port =8081)
