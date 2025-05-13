from flask import Flask, session, render_template, request, redirect, url_for, flash, jsonify
import psycopg2
import psycopg2.extras
import re
import os
from datetime import datetime, timedelta

PGHOST = 'ep-green-lake-a5nsemie.us-east-2.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = '4ZFkXlMWTJA2'
app = Flask(__name__)
db_connection_session = psycopg2.connect(dbname='Surgery_Department', user=PGUSER, password=PGPASSWORD, host=PGHOST,
                                         port=5432)
app.secret_key = '123'

@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/x-ray')
def x_ray():
    return render_template('x-ray.html')

@app.route('/MRI')
def mri():
    return render_template('MRI.html')

@app.route('/CT')
def ct():
    return render_template('CT.html')

@app.route('/US')
def US():
    return render_template('ultrasound.html')

@app.route('/founders')
def founders():
    return render_template('Founders.html')


@app.route('/loginPA', methods=['GET', 'POST'])
def login_pa():
    if request.method == 'GET':
        return render_template('loginPA.html')

    elif request.method == 'POST':
        email = request.form.get('Pemail')
        password = request.form.get('Ppassword')

        if not email or not password:
            flash('Please enter both email and password', 'error')
            return redirect(url_for('login_pa'))

        # Query the database for patient email and password
        cur = db_connection_session.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute('SELECT * FROM patient WHERE P_email = %s AND P_password = %s', (email, password))
        patient_data = cur.fetchone()
        if patient_data is None:
            flash('Incorrect email or password', 'error')
            return render_template('loginPA.html')
        else:
            # Store patient data and image filename in the session
            session['patient'] = patient_data
            
            return redirect(url_for('index'))


@app.route('/registerPA', methods=['GET', 'POST'])
def register_pa():
    if request.method == 'GET':
        return render_template('registerPA.html')

    elif request.method == 'POST':
        # Get form data
        SSN = request.form.get('SSN')
        first_name = request.form.get('fname')
        middle_name = request.form.get('mname')
        last_name = request.form.get('lname')
        gender = request.form.get('gender')
        date_of_birth = request.form.get('DOB')
        phone_number = request.form.get('phone')
        address = request.form.get('add')
        blood_type = request.form.get('bt')
        medical_history = request.form.get('mh')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')


        # Validate the form data
        if len(password) < 8:
            flash('Password must be at least 8 characters long', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        elif not SSN.isdigit() or len(SSN) != 14:
            flash('SSN is invalid', 'error')
        elif not phone_number.isdigit() or len(phone_number) != 11:
            flash('Phone number is invalid', 'error')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid email address', 'error')
        else:
            # Check if the email is already registered
            cur = db_connection_session.cursor()
            cur.execute('SELECT * FROM patient WHERE P_email = %s', (email,))
            if cur.fetchone():
                flash('Email already registered', 'error')
            else:
                
                cur.execute('''
                    INSERT INTO patient (
                        P_SSN, P_fname, P_mname, P_lname, P_gender, P_date_of_birth,
                        P_phone_No, P_address, blood_type, medical_history, P_email,
                        P_password
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''',
                            (SSN, first_name, middle_name, last_name, gender, date_of_birth,
                             phone_number, address, blood_type, medical_history, email,
                             password))
                db_connection_session.commit()
                flash('Registration successful', 'success')

        return redirect('/registerPA')