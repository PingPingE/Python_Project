from flask import Flask, url_for
app = Flask(__name__)
#url_for: 특정함수를 호출하는 URI찾기
@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))