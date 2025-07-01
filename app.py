from flask import Flask, render_template, request, redirect, flash
import pymysql
from werkzeug.security import generate_password_hash
import subprocess
import os
from flask import session
from werkzeug.security import check_password_hash
app = Flask(__name__)
app.secret_key = 'supersecretkey'

import os
db = pymysql.connect(
    host="db",  # container ismi
    user="root",
    password="1234",
    database="hasta_kayit"
)


cursor = db.cursor()
@app.route('/')
def home():
    return redirect('/login')


@app.route('/backup', methods=['GET', 'POST'])
def backup():
    message = ""
    if request.method == 'POST':
        try:
            result = subprocess.run(["python", "backup_script.py"], capture_output=True, text=True)
            if result.returncode == 0:
                message = "Backup başarıyla alındı."
            else:
                message = f"Hata oluştu: {result.stderr}"
        except Exception as e:
            message = f"Script çalıştırılırken hata: {e}"

    log_content = ""
    if os.path.exists("backup.log"):
        with open("backup.log", "r", encoding="utf-8", errors="ignore") as log_file:
            log_content = log_file.read()

    return render_template("backup.html", log=log_content, message=message)



@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        ad = request.form['ad']
        soyad = request.form['soyad']
        tc = request.form['tc']
        telefon = request.form['telefon']
        bolum = request.form['bolum']
        sikayet = request.form['sikayet']

        query = "INSERT INTO patients (ad, soyad, tc_kimlik_no, telefon, bolum, sikayet) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ad, soyad, tc, telefon, bolum, sikayet)

        try:
            cursor.execute(query, values)
            db.commit()
            flash('Hasta kaydı başarıyla oluşturuldu.', 'success')
        except Exception as e:
            db.rollback()
            flash(f'Hata oluştu: {e}', 'danger')

    return render_template('dashboard.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Giriş başarılı!', 'success')
            return redirect('/dashboard')
        else:
            flash('Geçersiz kullanıcı adı veya şifre.', 'danger')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_pw = generate_password_hash(password)

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_pw))
            db.commit()
            flash('Kayıt başarılı! Artık giriş yapabilirsiniz.', 'success')
            return redirect('/login')
        except Exception as err:
            db.rollback()
            flash(f'Hata oluştu: {err}', 'danger')

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

