from flask import Flask, request, render_template, send_from_directory, redirect,url_for

import os
files = set()
upload_directory = os.path.dirname(__file__)+'/files'
for filename in os.listdir(upload_directory):
    path= os.path.join(upload_directory,filename)
    if os.path.isfile(path):
        files.add(filename)

if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fileupload',methods=['GET','POST'])#파일 업로드하기
def upload_file():
    if request.method == 'POST':
        f=request.files['file']
        dirname = os.path.dirname(__file__)+'/files/'+f.filename#저장할 경로 + 파일명
        print("post   ", dirname)
        f.save(dirname)
        return redirect('/filelist')
    return render_template('fileupload.html')

@app.route('/filelist')
def list_files():
    for filename in os.listdir(upload_directory):
        path= os.path.join(upload_directory,filename)
        if os.path.isfile(path):
            files.add(filename)
    return render_template('fileview.html',files= files)
        
@app.route('/filelist/<path:path>')
def get_file(path):
    return send_from_directory(upload_directory,path, as_attachment=True)

@app.route('/fileview',methods=['GET','POST'])
def get_all_files():
    return render_template('fileview.html',files= files)

if __name__ == '__main__':
    app.run(debug=True,port=8077)