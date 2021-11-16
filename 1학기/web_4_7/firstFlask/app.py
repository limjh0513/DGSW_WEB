from flask import *

# __name__은 현재 시행되고 있는 모듈의 이름을 가르키는 예약어, 그냥 항상 이렇게 쓴다고 생각해도 됨
app = Flask(__name__)

def get_menu2(date):
    import requests

    # API 요청
    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    params = {
        'Type': 'json',
        'ATPT_OFCDC_SC_CODE': 'D10', # 시도교육청코드
        'SD_SCHUL_CODE': '7240454', # 표준학교코드
        'MLSV_YMD': date
    }
    r = requests.get(url, params=params)

    # JSON 파싱
    j = r.json()
    
    data = {
        'menu': j['mealServiceDietInfo'][1]['row']
    }
    
    return data

@app.route('/menu')
def menu():
    #flask.request
    
    # $_GET == request.args
    # $_POST == request.form
    # $_REQUEST = request.values
    
    mdate = request.values.get('date')
    # date값이 없으면 None, 오늘 날짜로 설정
    if mdate is None:
        from datetime import date
        mdate = date.today().strftime('%Y%m%d')
    
    '''menu_data = get_menu(mdate).replace('\n', '<br>')
    print(menu_data)'''
    
    menu_data = get_menu2(mdate)
    #menu_data['menu'] -> [(조식 식단표), (중식 식단표), ...]
    
    return render_template('menu.html', menu_data=menu_data)


# /경로로 들어왔을 때 실행할 함수
@app.route('/')
def index():
    return redirect('/menu')


#python 내장 웹서버로 실행
app.run(host='0.0.0.0', port=2000, debug=True)