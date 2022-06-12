import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime
import noti

def replyAptData(date_param, user, loc_param='대학', comm ='지역'): 
    print(user,comm, date_param, loc_param) 
    res_list = noti.getData(date_param , loc_param, comm)

    msg = '' 
    for r in res_list: 
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH: 
            noti.sendMessage( user, msg ) 
            msg = r+'\n' 
        else: 
            msg += r+'\n'

    if msg: 
        noti.sendMessage( user, msg ) 
    else: 
        noti.sendMessage( user, '%s 지역에 해당하는 요청이 없습니다.'%date_param)

def save( user, loc_param ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    
    try: 
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param)) 
    except sqlite3.IntegrityError: 
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' ) 
        return
    else: 
        noti.sendMessage( user, '저장되었습니다.' ) 
        conn.commit()

def check( user ): 
    conn = sqlite3.connect('users.db') 
    cursor = conn.cursor() 
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, locationTEXT, PRIMARY KEY(user, location) )') 
    cursor.execute('SELECT * from users WHERE user="%s"' % user)

    for data in cursor.fetchall(): 
        row = 'id:' + str(data[0]) + ', location:' + data[1] 
        noti.sendMessage( user, row )

def handle(msg): 
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text': 
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.') 
        return

    text = msg['text'] 
    args = text.split(' ')

 
    if text.startswith('지역') and len(args)>1: 
        print('try to 지역', args[1]) 
        replyAptData( args[1], chat_id, args[2] , '지역') 
    elif text.startswith('저장') and len(args)>1: 
        print('try to 저장', args[1]) 
        save( chat_id, args[1] ) 
    elif text.startswith('확인'): 
        print('try to 확인') 
        check( chat_id )
    else: 
        noti.sendMessage(chat_id, '''모르는 명령어입니다.
        - 도움말 -
        1. 학교 검색

          지역 [지역명][학교종류] 
            └ 예시 :: 지역 수원시 대학교  
                      지역 가평 초등
                      지역 광명 중학교 

        2. 내용 저장
          저장 [내용]

        3. 저장 내용 확인
        확인''')
        
today = date.today() 
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

from noti import bot
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...') 

while 1: 
    time.sleep(10)   