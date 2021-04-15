from flask import *

# __name__은 현재 시행되고 있는 모듈의 이름을 가르키는 예약어, 그냥 항상 이렇게 쓴다고 생각해도 됨
app = Flask(__name__)

from flaskext.mysql import MySQL
import pymysql

import os
os.environ['APP_SETTINGS'] = 'setting.cfg'

# flask에 설정파일이 있다고 알리기
app.config.from_envvar('APP_SETTINGS')

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)

# Flask 인스턴스와 연결
mysql.init_app(app)

@app.route('/delete/<pk>')
def guestbook_delete(pk):
    conn = mysql.get_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM guestbook WHERE pk = %s', (pk,))

    conn.commit()

    return redirect('/')

@app.route('/write', methods=['POST'])
def write():
    conn = mysql.get_db()
    cursor = conn.cursor()

    author = request.values.get('author', '').strip()
    content = request.values.get('content', '').strip()

    print(author)
    print(content)

        #컬럼 순서가 pk, author, content, inserted_at
        #pk에는 AUTOINCREMENT를 걸어 뒀으므로 null입력시 자동으로 숫자
        #inserted_at 에는 현재 작성 시간을 입력하기 위해 내장 함수 NOW() 사용
        # SQL Injection 방어를 위해 escape를 사용
        #쿼리문에 %s로 자리를 지정해주고 쿼리문 다음 인자로 해당 값을 넘겨주면 자동으로 escape

    if author != '' and content != '':

        cursor.execute('INSERT INTO guestbook VALUES (NULL, %s, %s, NOW());', (author, content,))

        #db 변경사항 반영
        conn.commit()
        #변경사항 반영하지 않으려면  conn.rollback()
        # POST일 경우에만 실행되는 if문 끝

    return redirect('/')
        

@app.route('/', methods=['GET'])
def index():
    conn = mysql.get_db()
    cursor = conn.cursor()
    
    # 작성된 게시글 가져오기
    cursor.execute('SELECT * FROM guestbook')
    rows = cursor.fetchall()
    for row in rows:
        # XSS 공격을 방지하기 위해 html 특수문자를 내가 직접 바꿔줘야함
        #TODO
        
        # 그 다음에 개행문자를 <br>태그로 변경
        row['inserted_at'] = row['inserted_at'].strftime('%Y-%m-%d %H:%M:%S')
        row['content'] = row['content'].replace('\n', '<br>\n')
    
    # GET이든, POST든 index.html 파일을 반환
    return render_template('index.html', rows=rows)


app.run(host='0.0.0.0', port=5000, debug=True)