from flask import Flask, render_template, request
from werkzeug.utils import secure_filename 
import os
app = Flask(__name__)

ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg','pdf'])
app.config['UPLOAD_FOLDER'] = ('uploads')

#pengecekan file degan menggunakan rsplit
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION
   
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        file = request.files['file']

        if 'file' not in request.files:
            return render_template('upload1.html')

        if file.filename == '':
            return render_template('upload1.html')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],  filename))            
            return  'file ' + filename +' di simpan' + ' <a href="/upload">kembali</a>'

    return render_template('upload1.html')

app.run(debug=True)