from flask import *
app = Flask(__name__)
import time

#편의 상 전역변수로, 실제 개발할 때에는 이런식으로 하면 안됨
chats = []

@app.route('/')
def index():
    return render_template('chat.html', chats=chats)

@app.route('/chat/data')
def chat_data():
    last_chat = request.values.get('last_chat')
    #request.values는 항상 문자열 혹은 None
    #값이 없거나 숫자가 아닐 수가 있음

    try:
        last_chat = int(last_chat)
    except:
        last_chat = 0


    # time.sleep(초) - 해당 초만큼 대기
    # time.sleep(초)

    # 클라이언트에게 없는 최신 채팅만 보내주기
    #new_chats = chats[last_chat:]

    #클라이언트가 받아간 이후 새 채팅이 있다면 바로 응답
    if last_chat != len(chats):
        pass
    else: # 클라이언트가 받아간 이후 새 채팅이 없음
        for i in range(10):
            # 1초씩 10번 쉬는 동안 새 채팅이 생기면 루프를 빠져나감
            if(last_chat != len(chats)):
                break;
            time.sleep(1)

    new_chats = chats[last_chat:]
    return{'chats' : new_chats, 'last_chat' : len(chats)}

@app.route('/chat/write', methods=['POST'])
def chat_write():
    content = request.values.get('content','')

    #저장
    chats.append(content)

    #원래 세팅 목록 페이지로 이동
    #return redirect('/')

    return {'result': 'sucess'}


# 젤 아래에 위치!
app.run(host='0.0.0.0', port=5000, debug=True)