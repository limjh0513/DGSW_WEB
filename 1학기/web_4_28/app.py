from flask import *
app = Flask(__name__)

from flaskext.mysql import MySQL
import pymysql

import os
os.environ['APP_SETTINGS'] = 'setting.cfg'

app.config.from_envvar('APP_SETTINGS')

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)

mysql.init_app(app)

@app.route('/join.html/join', methods=['POST'])
def join():
    conn = mysql.get_db()
    cursor = conn.cursor()

    id = request.values.get('user_id')
    password = request.values.get('user_pw')
    name = request.values.get('user_name')
    idCheck = 0

    cursor.execute('SELECT * FROM user2 WHERE user_id = %s', [id])
    row = cursor.fetchone()

    if(row is None):
        cursor.execute('INSERT INTO user2 VALUES (NULL, %s, %s, %s);', [id, name, password])
        conn.commit()

        return redirect('/login.html')
    else:
        message = '이미 가입된 ID입니다.'
        return render_template('join.html', error=message)

    
@app.route('/index.html/logout')
def logout():
    session['name'] = None
    return render_template('/index.html')


@app.route('/login.html/login', methods=['POST'])
def login():
    conn = mysql.get_db()
    cursor = conn.cursor()

    id = request.values.get('user_input_id')
    password = request.values.get('user_input_pw')

    cursor.execute('SELECT * FROM user2 WHERE user_id = %s AND user_pw = %s', [id, password])
    row = cursor.fetchone()
    # 있으면 값이 반환되지만 없으면 None

    print(row)
    
    if (row is not None):
        # session 에 값 설정
        user = row['user_name']
        session['name'] = user
        return render_template('/index.html', name = user)
    else:
        message = 'ID, 비밀번호가 올바르지 않습니다.'
        return render_template('login.html', error=message)

    # for row in rows:
    #     print(row)
    #     if(row.user_id == id and row.user_pw == password):
    #         check = 1


@app.route('/')
def rutePage():
    name = session.get('name')
    return render_template('/index.html', name = name)

@app.route('/index.html')
def indexPage():
    name = session.get('name')
    return render_template('/index.html', name = name)

@app.route('/login.html')
def loginPage():
    return render_template('login.html')

@app.route('/join.html')
def joinPage():
    return render_template('join.html')

@app.route('/index_logged.html')
def LoginedPage():
    return render_template('index_logged.html')



app.run(host='0.0.0.0', port=5000, debug=True)