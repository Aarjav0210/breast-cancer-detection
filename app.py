import os
import psycopg2
from urllib import response
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from script import process_csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from dotenv import load_dotenv


load_dotenv()

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


conn = psycopg2.connect(os.getenv("DATABASE_URL"))

logged_in = False

with conn.cursor() as cur:
    cur.execute("SELECT now()")
    res = cur.fetchall()
    conn.commit()
    print(res)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        input_file = request.files['input_file']
        if input_file and allowed_file(input_file.filename):
            input_filename = secure_filename(input_file.filename)
            new_filename = f'{input_filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = os.path.join('input_files', new_filename)
            input_file.save(save_location)
            process_csv(save_location)
        return redirect(url_for('results'))
    
    return render_template('upload.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        message = Mail(from_email='curavue@gmail.com',
                        to_emails='curavue02@gmail.com',
                        subject='Your results file is ready...',
                        plain_text_content='Please access your results file here',
                        html_content='Your results file are ready to be downloaded here',
                        )
        try:
            sg = SendGridAPIClient(os.getenv("SENDGRID_API"))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        return redirect(url_for('results'))

    return render_template('results.html')

@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # email = request.form.get('inputEmail')
        # with conn.cursor() as cur:
        #     selectstatement = '''SELECT * FROM user_data Where "email" = %s'''
        #     password_hash = cur.execute(selectstatement, (email,))
        #     conn.commit()
        #     print(password_hash)
        # if check_password_hash(password_hash, request.form.get('inputPassword')):
            logged_in = True
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('inputName')
        email = request.form.get('inputEmail')
        password_hash = generate_password_hash(request.form.get('inputPassword'))

        with conn.cursor() as cur:
            try:
                cur.execute("INSERT INTO user_data (email, name, password) VALUES(%s, %s, %s)", (email, name, password_hash))
                conn.commit()
                cur.execute("SELECT * FROM user_data")
                res = cur.fetchall()
                conn.commit()
                print(res)
                logged_in = True
            except Exception as e:
                print("This user already exists")

    return render_template('signup.html')

@app.route('/myaccount', methods=['GET', 'POST'])
def myaccount():
        

    return render_template('myaccount.html')