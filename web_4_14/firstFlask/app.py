from flask import *
app = Flask(__name__)

#세션사용을 위해 암호화키 설정



# pip install flask-mysql
from flaskext.mysql import MySQL
import pymysql

app.config['MYSQL_DATABASE_HOST'] = 'web.dgsw.kr'


#설정파일(setting.cfg)파일을 만들고 환경변수에 설정파일의 경로 적어주기
# bash쉘 : export APP_SETTINGS=settings.cfg
# 윈도우 : set APP_SETTINGS=settings.cfg

import os
os.environ['APP_SETTINGS'] = 'setting.cfg'

# flask에 설정파일이 있다고 알리기
app.config.from_envvar('APP_SETTINGS')

# DB연결 정보 입력

# mysql = MySQL(host='web.dgsw.kr', port=3306, 
#                 user='s2115', password='21152115', 
#                 db='s2115', 
#                 cursorclass=pymysql.cursors.DictCursor )

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)

# Flask 인스턴스와 연결
mysql.init_app(app)


@app.route('/session/set')
def session_set():
    #session['name']='임재현'
    print(request.values.get('name', ''))
    session['name'] = request.values.get('name', '')

    return 'ok'

@app.route('/session/get')
def session_get():
    #name = seesion['name']
    #값이 없으면 오류가 나게 됨
    #세션이 있는지 if로 확인하거나 기본값을 지정해서 받아오기

    #if 'name' in session:
    name = session.get('name','기본값')
    #값이 없을 경우 None


    return name


@app.route('/')
def index():
    # DB 연결 정보 가져오기
    conn = mysql.get_db()
    # Cursor 가져오기
    cursor = conn.cursor()
    # 쿼리 실행
    cursor.execute('SELECT * FROM users')
    
    #cursor.fetchall() -> 응답 결과 전부
    #cursor.fetchone() -> 한개만
    users = cursor.fetchall()
    
    # 결과 반환용 변수 생성
    #result = {'users': list(users)}
    #return result
    
    '''
    DictCursor를 안 쓸 경우:
    users = [
        [1, "admin", "2345"], -> user
        [2, "guest", "5678"]  -> user
    ]
    
    DictCursor를 쓸 경우:
    users: [
        {
          "pk": 1, 
          "user_id": "admin", 
          "user_pw": "2345"
        }, 
        {
          "pk": 2, 
          "user_id": "guest", 
          "user_pw": "5678"
        }
    ]
    '''
    content = ''
    for user in users:
        #content += '사용자ID: ' + user[1] + '<br>'
        content += '사용자ID: ' + user['user_id'] + '<br>'
    
    return content
    

# 젤 아래에 위치!
app.run(host='0.0.0.0', port=5000, debug=True)