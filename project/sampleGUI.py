from os import scandir
from socket import AddressFamily
from tkinter import *
from tkinter import font
from tkinter import ttk
from xml.etree import ElementTree
from email.mime.text import MIMEText
import tkintermapview
import pickle

g_Tk = Tk()
mp=None
bm=None
addE=None
g_Tk.title("학교종이 땡땡땡")

img = PhotoImage(file='image/Title.png')
img1 = PhotoImage(file='image/Search.png')
img2 = PhotoImage(file='image/BookMark.png')
img3 = PhotoImage(file='image/map.png')

BookMarkList=[]
def event_for_listbox(event): # 리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        OnSchool(data.split()[1])

def event_for_BookMarklistbox(event): # 북마크리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        OnSchool(event.widget.get(selection))


def InitScreen(): 
    f=open('BookMark.txt','ab')
    f.close()
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family = '나눔고딕')
    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    fontin = font.Font(g_Tk, size=13, weight='bold')

    # 화면 전체 구도 잡기. 
    frameTitle = Frame(g_Tk, bg='#fffbd2')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#fffbd2')
    frameCombo.pack()
    frameEntry = Frame(g_Tk, pady=10, bg='#fffbd2')
    frameEntry.pack(side="top", fill="x")
    framebotton = Frame(g_Tk, pady=10, bg='#fffbd2')
    framebotton.pack(side="top", fill="both", expand=True)
    global frameResult
    frameResult = Frame(g_Tk, padx=10, pady=10, bg='#fffbd2')
    frameResult.pack(side="bottom", fill="both", expand=True)


    # title 부분
    titleimg = Label(frameTitle,image=img,bg='#fffbd2',text="초등학교")
    titleimg.pack(fill="both",expand=True, anchor = "center")


    # 종류 선택 부분
    radioValue = IntVar()
    global rcheck
    rcheck = 0
    r1 = Radiobutton(frameCombo, font=fontNormal, value=0, variable=radioValue, text="초등학교", command=lambda:CheckRadio(0), bg='#fff7a9',activebackground= '#fff481',) 
    r1.pack(side='left',expand=True, fill="both")
    
    r2 = Radiobutton(frameCombo, font=fontNormal, value=1, variable=radioValue, text="중학교", command=lambda:CheckRadio(1), bg='#fff7a9',activebackground = '#fff481') 
    r2.pack(side='left',expand=True, fill="both")

    r3 = Radiobutton(frameCombo, font=fontNormal, value=2, variable=radioValue, text="고등학교", command=lambda:CheckRadio(2), bg='#fff7a9',activebackground = '#fff481') 
    r3.pack(side='left',expand=True, fill="both")

    r4 = Radiobutton(frameCombo, font=fontNormal, value=3, variable=radioValue, text="대학교/대학원", command=lambda:CheckRadio(3), bg='#fff7a9',activebackground = '#fff481') 
    r4.pack(side='left',expand=True, fill="both")

    r5 = Radiobutton(frameCombo, font=fontNormal, value=4, variable=radioValue, text="모두", command=lambda:CheckRadio(4), bg='#fff7a9',activebackground = '#fff481') 
    r5.pack(side='left',expand=True, fill="both")
    

    # 사용자 입력 부분
    global InputLabel
    InputLabel = Entry(frameEntry, fg ='#ffaa00',selectbackground = "#ff6010",bg='White',
    insertbackground = '#ff6010',font = fontNormal,width = 37, borderwidth = 3, relief = 'sunken')
    InputLabel.pack(side="left", padx=9, expand=True)

    SearchButton = Button(frameEntry, font = fontNormal, \
    text="검색", command=onSearch,image=img1,)
    SearchButton.pack(padx = 5,expand=True)

    # 버튼 3개
    global LocalCombo
    Local_str = ['모두']
    Local_List_add(Local_str)
    LocalCombo = ttk.Combobox(framebotton,justify = 'center',foreground="#ffaa00",font=fontin, values = Local_str)
    LocalCombo.pack(side="left", padx=12,expand=True, fill='both')
    LocalCombo.set("모두")
    
    SearchButton = Button(framebotton, font = fontNormal,image=img3,  width = 100,text="지도", command=OnMap)
    SearchButton.pack(side="right", padx=5, fill='both')
    SearchButton = Button(framebotton, font = fontNormal,image=img2,  width = 100,text="북마크",command=OnBookMark)
    SearchButton.pack(side="right", padx=5, fill='both')


    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameResult)
    listBox = Listbox(frameResult, selectmode='extended',fg ="#ffaa00",selectforeground='White',selectbackground = "#ffaa00",
        font=fontNormal, width=25, height=15, bg= 'White',\
        borderwidth=2, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=False, fill="x")
    
    LBScrollbar.pack(side="left", fill='y')
    LBScrollbar.config(command=listBox.yview)

    # 그래프

def drawGraph(canvas,data,canvasWidth,canvasHeight):
    canvas.delete(ALL)

    nData = len(data)
    nMax = max(data)
    nMin=min(data)

    canvas.create_rectangle(0,0,canvasWidth,canvasHeight,fill='White',tag='gp')

    if nMax==0:
        nMax=1
    
    rectWidth = (canvasWidth//nData)
    bottom = canvasHeight - 20
    maxheight = canvasHeight - 40
    for i in range(nData):
        if nMax == data[i]:color="#fff052"
        elif nMin == data[i]:color="#fffaca"
        else:color="#fff7a9"

        curHeight = maxheight * data[i]/nMax
        top = bottom - curHeight
        left = i*rectWidth
        right=(i+1)*rectWidth
        canvas.create_rectangle(left,top,right,bottom,fill=color,tag='gp',activefill='#cbff52')

        canvas.create_text((left+right)//2,top-10,text=data[i],tags='gp')
        canvas.create_text((left+right)//2,bottom+10,text=i+1,tags='gp')
def CheckRadio(num):
    global rcheck
    rcheck = num


def onSearch(): # "검색" 버튼 이벤트처리
    global rcheck
    SearchLibrary(rcheck) 

def OnBookMark():              # 북마크 팝업
    global g_Tk,BookMarkList,bm
    f=open('BookMark.txt','rb')
    while True:
        try :    
            BookMarkList=pickle.load(f)
        except EOFError:
            f.close()
            break

    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    bm=Toplevel(g_Tk)
    bm.title("북마크")

    bmframe = Frame(bm, bg='#d6f2ff',padx=10, pady=10)
    bmframe.pack(side="bottom", fill="both")

    bmLBScrollbar = Scrollbar(bmframe)
    bmlistBox = Listbox(bmframe, selectmode ='extended',fg ="#ffaa00",selectforeground='White',selectbackground = "#ffaa00",
        font=fontNormal, width=20, height=15, bg= 'White',\
        borderwidth=2, relief='ridge', yscrollcommand=bmLBScrollbar.set)
    cnt=0
    for i in BookMarkList:
        bmlistBox.insert(cnt,i)
        cnt+=1
    
    bmlistBox.bind('<<ListboxSelect>>', event_for_BookMarklistbox)
    bmlistBox.pack(side='left', anchor='n', expand=False, fill="x")

    bmLBScrollbar.pack(side='left',fill='y')
    bmLBScrollbar.config(command=listBox.yview)

    ClearButton = Button(bmframe, font = fontNormal,text="초기화",command = Clear)
    ClearButton.pack(side="left", padx=10, pady=5)

def Clear():
    global BookMarkList,bm
    BookMarkList=[]
    f=open('BookMark.txt','wb')
    pickle.dump(BookMarkList,f)
    f.close()
    bm.destroy()

def AddBookMark(name):               # 북마크 추가
    global BookMarkList,bm
    f=open('BookMark.txt','rb')
    while True:
        try :    
            BookMarkList=pickle.load(f)
        except EOFError:
            f.close()
            break
    if (name not in BookMarkList):
        f=open('BookMark.txt','wb')
        BookMarkList.append(name)
        pickle.dump(BookMarkList,f)
        f.close()
    else:
        BookMarkList.remove(name)
        f=open('BookMark.txt','wb')
        pickle.dump(BookMarkList,f)
        f.close()
    bm.destroy()

def OnSchool(name):              # 학교 팝업
    global g_Tk,BookMarkList
    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    fontTitle = font.Font(g_Tk, size=25, weight='bold',family = "나눔고딕")
    sc=Toplevel(g_Tk)
    sc.title(name)

    # 화면 전체 구도 잡기. 
    frameTitle = Frame(sc, bg='#fffbd2')
    frameTitle.pack(side="top", fill="x")

    titleimg = Label(frameTitle,font = fontTitle, bg='#fffbd2',text=name, fg= "#ff9d00")
    titleimg.pack(fill="both",expand=True, anchor = "w")

    frameinfo = Frame(sc, pady=10, bg='#fffbd2')
    frameinfo.pack()
    framebotton = Frame(sc, pady=10, bg='#fffbd2')
    framebotton.pack(side="bottom", fill="both", expand=True)
    f=open('BookMark.txt','rb')
    while True:
        try :    
            BookMarkList=pickle.load(f)
        except EOFError:
            f.close()
            break
    if(name in BookMarkList):
        BookButton = Button(framebotton, font = fontNormal,text="북마크 삭제", command = lambda : AddBookMark(name))
        BookButton.pack(side="left", padx=10, pady=5)
    else:
        BookButton = Button(framebotton, font = fontNormal,image=img3, text="북마크 추가", command = lambda : AddBookMark(name))
        BookButton.pack(side="left", padx=10, pady=5)
    MailButton = Button(framebotton, font = fontNormal,image=img2, text="메일",command= OnMail)
    MailButton.pack(side="right", padx=10, pady=5)

    infoBox = Listbox(frameinfo, selectmode='extended',fg ="#ffaa00",selectforeground='White',selectbackground = "#ffaa00",
        font=fontNormal,width=40, height=15, bg= 'White',\
        borderwidth=2, relief='ridge')
    infoBox.bind('<<ListboxSelect>>', event_for_listbox)
    infoBox.pack(side='left', anchor='n', padx=10, expand=False, fill="x")


def OnMail():         #메일 보내기 팝업
    global g_Tk
    mp = Toplevel(g_Tk)
    mp.title("이메일 주소 입력")

    inputmail = Entry(mp,width=50)
    inputmail.pack(fill='x',pady = 10,expand=True)
    
    msg = MIMEText('본문: ㅎㅇ')
    msg['Subject'] = '제목 : 함보'
    senderAddr = 'lsy0112114@gmail.com'
    recipientAddr = 'lsy0112114@gmail.com'

    bt = Button(mp,text = "보내기",command = lambda : SendMail(senderAddr,recipientAddr,msg))
    bt.pack(anchor="s",padx=10,pady=10)

def SendMail(fromAddr,toAddr,msg):
    import smtplib
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()

    s.login('lsy0112114@gmail.com','fozxzasvghelpqvo')
    s.sendmail(fromAddr,[toAddr],msg.as_string())
    s.close()


def OnMap():              # 지도 팝업
    global g_Tk
    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    map=Toplevel(g_Tk)
    map.title("지도")

    searchframe = Frame(map, bg='#c7ffa6',padx=10, pady=10)
    searchframe.pack(side="top", fill="both")
    mapframe = Frame(map, bg='#d6f2ff',padx=10, pady=10)
    mapframe.pack(side="top", fill="both")

    global InputLabel_Map
    InputLabel_Map = Entry(searchframe, fg ='#6cce32',selectbackground = "#dcffc8",bg='White',
    insertbackground = '#487c2a',selectforeground='#487c2a',font = fontNormal,width = 30, borderwidth = 5, relief = 'sunken')
    InputLabel_Map.pack(side="left", padx=10, expand=True, fill='x')

    SearchButton_Map = Button(searchframe, font = fontNormal, \
    text="검색", command=onSearch_Map,image=img1,)
    SearchButton_Map.pack(side="right")

    global marker_1, map_widget
    map_widget = tkintermapview.TkinterMapView(mapframe, 
    width=800, height=500, corner_radius=0) 
    map_widget.pack()

    # marker_1 = map_widget.set_position(37.8599522344, 127.5144681238, marker=True)# 위도,경도 위치지정
    # 주소 위치지정 
    marker_1 = map_widget.set_address("경기도 시흥시 산기대학로 237", marker=True)
    # print(marker_1.position, marker_1.text) # get position and text 
    marker_1.set_text("한국공학대학교") # set new text 
    map_widget.set_zoom(13) # 0~19 (19 is the highest zoom level)

def onSearch_Map():
    SearchLibrary(4, True)

def getStr(s): 
    return '' if not s else s

def SearchLibrary(chk, onMap=False): # "검색" 버튼 -> "도서관"
    global listBox, LocalCombo
    gplist = [0,0,0,0]
    listBox.delete(0,listBox.size()) 
    School_text = ""
    if chk == 0:
        School_text = "초등학교"
    elif chk == 1:
        School_text = "중학교"
    elif chk == 2:
        School_text = "고등학교"
    elif chk == 3:
        School_text = "대학"
    else:
        School_text = "모두"
    if chk == 4:
        if onMap:
            with open('xml/초중고등학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
                parseData = ElementTree.fromstring(strXml) 
                
                elements = parseData.iter('row')
                    
                for item in elements: # " row“ element들
                    part_el = item.find('SIGUN_NM')
                    part_el2 = item.find('FACLT_NM')

                    if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text \
                        or InputLabel_Map.get() not in part_el2.text: 
                        continue

                    marker_1 = map_widget.set_position(float(item.find('REFINE_WGS84_LAT').text),
                    float(item.find('REFINE_WGS84_LOGT').text), marker=True)
                    marker_1.set_text(part_el2.text) # set new text
                    map_widget.set_zoom(13) # 0~19 (19 is the highest zoom level)
            
            with open('xml/전문및대학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
                parseData = ElementTree.fromstring(strXml) 
                
                elements = parseData.iter('row')
                    
                for item in elements: # " row“ element들
                    part_el = item.find('SIGUN_NM')
                    part_el2 = item.find('FACLT_NM')

                    if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text \
                        or InputLabel_Map.get() not in part_el2.text: 
                        continue
                    
                    marker_1 = map_widget.set_position(float(item.find('REFINE_WGS84_LAT').text),
                    float(item.find('REFINE_WGS84_LOGT').text), marker=True)
                    marker_1.set_text(part_el2.text) # set new text 
                    map_widget.set_zoom(13) # 0~19 (19 is the highest zoom level)

        else:
            with open('xml/초중고등학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
                parseData = ElementTree.fromstring(strXml) 

                elements = parseData.iter('row')

                i = 1
                for item in elements: # " row“ element들
                    part_el = item.find('SIGUN_NM')
                    part_el2 = item.find('FACLT_NM')
                    SCHOOL_DIV = item.find('SCHOOL_DIV_NM')

                    if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text \
                        or InputLabel.get() not in part_el2.text: 
                        continue 

                    _text = '[' + str(i) + '] ' + \
                        getStr(item.find('FACLT_NM').text)
                    listBox.insert(i-1, _text)
                    i = i+1
                    if ("초등학교" in SCHOOL_DIV.text): gplist[0]+=1
                    elif ("중학교" in SCHOOL_DIV.text): gplist[1]+=1
                    else : gplist[2]+=1

            with open('xml/전문및대학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
                parseData = ElementTree.fromstring(strXml) 

                elements = parseData.iter('row')

                i = 1
                for item in elements: # " row“ element들
                    part_el = item.find('SIGUN_NM')
                    part_el2 = item.find('FACLT_NM') 

                    if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text \
                        or InputLabel.get() not in part_el2.text: 
                        continue 

                    _text = '[' + str(i) + '] ' + \
                        getStr(item.find('FACLT_NM').text)
                    listBox.insert(i-1, _text)
                    i = i+1
                    gplist[3]+=1

    else:
        if not chk == 3:
            with open('xml/초중고등학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
            parseData = ElementTree.fromstring(strXml) 
            
            elements = parseData.iter('row')
                
            i = 1
            for item in elements: # " row“ element들
                part_el = item.find('SIGUN_NM')
                part_el2 = item.find('FACLT_NM')
                SCHOOL_DIV = item.find('SCHOOL_DIV_NM')
                # if InputLabel.get() not in part_el.text or School_text not in SCHOOL_DIV.text: 
                #     continue 
            
                if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text or School_text not in SCHOOL_DIV.text \
                    or InputLabel.get() not in part_el2.text: 
                    continue 
            
                _text = '[' + str(i) + '] ' + \
                    getStr(item.find('FACLT_NM').text)
                listBox.insert(i-1, _text)
                i = i+1
                if ("초등학교" in SCHOOL_DIV.text): gplist[0]+=1
                elif ("중학교" in SCHOOL_DIV.text): gplist[1]+=1
                else : gplist[2]+=1
        else:
            with open('xml/전문및대학교현황.xml', 'rb') as f: 
                strXml = f.read().decode('utf-8')
            parseData = ElementTree.fromstring(strXml) 
            
            elements = parseData.iter('row')

            i = 1
            for item in elements: # " row“ element들
                part_el = item.find('SIGUN_NM')
                part_el2 = item.find('FACLT_NM')

                if not LocalCombo.get() == "모두" and LocalCombo.get() not in part_el.text \
                    or InputLabel.get() not in part_el2.text: 
                    continue 
            
                _text = '[' + str(i) + '] ' + \
                    getStr(item.find('FACLT_NM').text)
                listBox.insert(i-1, _text)
                i = i+1
                gplist[3]+=1

    graph = Canvas(frameResult,bg='Red',width = 200)
    graph.delete('gp')
    graph.place(x=310,y=0 ,width=210,height=380,anchor= "nw")
    drawGraph(graph, gplist, 210, 400)

def Local_List_add(locallist):
    with open('xml/초중고등학교현황.xml', 'rb') as f: 
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml) 
        
    elements = parseData.iter('row')


    for item in elements: # " row“ element들
        part_el = item.find('SIGUN_NM')
        if part_el.text in locallist: 
            continue 
        locallist.append(part_el.text)

    with open('xml/전문및대학교현황.xml', 'rb') as f: 
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml) 
        
    elements = parseData.iter('row')
            
    for item in elements: # " row“ element들
        part_el = item.find('SIGUN_NM')
        if part_el.text in locallist: 
            continue 
        locallist.append(part_el.text)
    
    

InitScreen()
g_Tk.mainloop()