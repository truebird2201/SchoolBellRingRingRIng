import sys
import telepot
from pprint import pprint 
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString

schoolkey = 'c7c84da8feb844a1a455d734bf220b48'
universitykey = 'ab579728f48e403cb9312b8d10f86c03'
TOKEN = '5584645645:AAHxsfkTRqlRxCBYg8ZIOG4PreCaFdt_1TA'
MAX_MSG_LENGTH = 300
bot = telepot.Bot(TOKEN)

def getData(date_param , loc_param,  comm): 
    res_list = [] 
    # url = baseurl+'&LAWD_CD='+loc_param+'&DEAL_YMD='+date_param
    
    
    # 대학 'https://openapi.gg.go.kr/Jnclluniv?KEY=c7c84da8feb844a1a455d734bf220b48&pIndex=1&pSize=252'
    # 초중고 'https://openapi.gg.go.kr/GgSchoolM?KEY=ab579728f48e403cb9312b8d10f86c03&pIndex=1&pSize=2389'

    if comm == '지역':
        if '대학' in loc_param:
            url = 'https://openapi.gg.go.kr/Jnclluniv?KEY='+ schoolkey + '&pIndex=1&pSize=252'
        else : # 2389
            url = 'https://openapi.gg.go.kr/GgSchoolM?KEY='+ universitykey + '&pIndex=1&pSize=1000'


    res_body = urlopen(url).read() 
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    items = tree.iter("row") # return list type
    for item in items: 
        local = item.find("SIGUN_NM").text
        name = item.find("SCHOOL_DIV_NM").text
        fac = item.find("FACLT_NM").text
        div = item.find("PLVTINST_DIV_NM").text
        Lot = item.find("REFINE_LOTNO_ADDR").text
        Roa = item.find("REFINE_ROADNM_ADDR").text
        zip = item.find("REFINE_ZIP_CD").text

        if '지역' in comm:
            if loc_param in name and date_param in local:
                row = name+ "  " + fac + " " + div +" \n"+ Lot + " \n" + Roa + "\n우편번호: "+zip +  " \n"
                res_list.append(row)


    return res_list

def sendMessage(user, msg): 
    try:
        bot.sendMessage(user, msg) 
    except: 
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)   