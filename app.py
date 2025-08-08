from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dealer = request.form.get('dealer')
        vin = request.form.get('vin')
        km = request.form.get('km')
        notes = request.form.get('notes')
        email = request.form.get('email')
        phone = request.form.get('phone')
        images = request.files.getlist('images')

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Submission from {dealer} - {vin} - {km}km at {timestamp}")

        for img in images:
            if img:
                filename = secure_filename(img.filename)
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Appraisal submitted successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")
    
