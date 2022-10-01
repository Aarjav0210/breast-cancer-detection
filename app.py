import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
# from script import process_csv

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello World!"

    @app.route('/input', methods=['GET', 'POST'])
    def input():
        if request.method == 'POST':
            input_file = request.files['file']
            if input_file and allowed_file(input_file.filename):
                input_filename = secure_filename(input_file.filename)
                new_filename = f'{input_filename.split(".")[0]}_{str(datetime.now())}.csv'
                save_location = os.path.join('input_files', new_filename)
                input_file.save(save_location)
            return redirect(url_for('results'))
        
        return render_template('input.html')

    @app.route('/results', methods=['GET', 'POST'])
    def results():
        if request.method == 'POST':
            
            return redirect(url_for('output'))

        return render_template('results.html')

    return app