from tkinter import *
from tkinter import font
g_Tk = Tk()
# g_Tk.geometry("400x600+450+100") # {width}x{height}+-{xpos}+-{ypos}


def event_for_listbox(event): # 리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)


def InitScreen(): 
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family = '나눔고딕')
    fontNormal = font.Font(g_Tk, size=15, weight='bold')

    # 화면 전체 구도 잡기. 
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#ff0000')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#00ff00')
    frameCombo.pack()
    frameEntry = Frame(g_Tk, pady=10, bg='#0000ff')
    frameEntry.pack(side="top", fill="x")
    framebotton = Frame(g_Tk, padx=10, pady=10, bg='#0ff0f0')
    framebotton.pack(side="top", fill="both", expand=True)
    frameResult = Frame(g_Tk, padx=10, pady=10, bg='#ffff00')
    frameResult.pack(side="bottom", fill="both", expand=True)

    # title 부분
    MainText = Label(frameTitle, font = fontTitle, text="학교종이 땡땡땡")
    MainText.pack(anchor="center", fill="both")

    # 종류 선택 부분
    radioValue = IntVar()
    global rcheck
    rcheck = 0
    r1 = Radiobutton(frameCombo, font=fontNormal, value=0, variable=radioValue, text="초등학교", command=lambda:CheckRadio(0)) 
    r1.pack(side='left',expand=True, fill="both")
    
    r2 = Radiobutton(frameCombo, font=fontNormal, value=1, variable=radioValue, text="중학교", command=lambda:CheckRadio(1)) 
    r2.pack(side='left',expand=True, fill="both")

    r3 = Radiobutton(frameCombo, font=fontNormal, value=2, variable=radioValue, text="고등학교", command=lambda:CheckRadio(2)) 
    r3.pack(side='left',expand=True, fill="both")

    r4 = Radiobutton(frameCombo, font=fontNormal, value=3, variable=radioValue, text="대학교/대학원", command=lambda:CheckRadio(3)) 
    r4.pack(side='left',expand=True, fill="both")
    
    
    sendEmailButton = Button(frameCombo, font = fontNormal, text='이메일') 
    sendEmailButton.pack(side='right', padx=10, fill='y')

    # 사용자 입력 부분
    global InputLabel
    InputLabel = Entry(frameEntry, font = fontNormal,width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack(side="left", padx=10, expand=True)

    SearchButton = Button(frameEntry, font = fontNormal, \
    text="검색", command=onSearch)
    SearchButton.pack(side="right", padx=10, expand=True, fill='y')

    # 버튼 3개
    SearchButton = Button(framebotton, font = fontNormal, text="지역")
    SearchButton.pack(side="left", padx=10, expand=True, fill='y')
    SearchButton = Button(framebotton, font = fontNormal, text="북마크", command=OnBookMark)
    SearchButton.pack(side="left", padx=10, expand=True, fill='y')
    SearchButton = Button(framebotton, font = fontNormal, text="지도")
    SearchButton.pack(side="left", padx=10, expand=True, fill='y')

    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameResult)
    listBox = Listbox(frameResult, selectmode='extended',\
        font=fontNormal, width=20, height=15, \
        borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set, bg='#ffa640',selectbackground='#fa8341')
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=False, fill="x")
    
    LBScrollbar.pack(side="left", fill='y')
    LBScrollbar.config(command=listBox.yview)

    #지도
    pass

def CheckRadio(num):
    global rcheck
    rcheck = num


def onSearch(): # "검색" 버튼 이벤트처리
    global rcheck
    print(rcheck)
    if rcheck == 0:
        SearchLibrary(rcheck)
    elif rcheck == 1:
        SearchLibrary(rcheck) 
    elif rcheck == 2:
        SearchLibrary(rcheck) 
    elif rcheck == 3:
        SearchLibrary(rcheck) 

def OnBookMark():              # 북마크 팝업
    global g_Tk
    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    bm=Toplevel(g_Tk)
    bm.title("북마크")
    bmframe = Frame(bm, padx=10, pady=10, bg='White')
    bmframe.pack(side="bottom", fill="both")
    bmLBScrollbar = Scrollbar(bmframe)
    bmlistBox = Listbox(bmframe, selectmode='extended',\
        font=fontNormal, width=20, height=15, \
        borderwidth=12, relief='ridge', yscrollcommand=bmLBScrollbar.set, bg='#ffa640',selectbackground='#fa8341')
    bmlistBox.bind('<<ListboxSelect>>', event_for_listbox)
    bmlistBox.pack(anchor='n', expand=False, fill="x")
    
    bmLBScrollbar.pack(side='right',fill='y')
    bmLBScrollbar.config(command=listBox.yview)

def getStr(s): 
    return '' if not s else s

def SearchLibrary(chk): # "검색" 버튼 -> "도서관"
    from xml.etree import ElementTree 
    
    global listBox
    listBox.delete(0,listBox.size()) 
    School_text = ""
    if chk == 0:
        School_text = "초등학교"
    elif chk == 1:
        School_text = "중학교"
    elif chk == 2:
        School_text = "고등학교"
    else:
        School_text = "대학"

    if not chk == 3:
        with open('project/xml/초중고등학교현황.xml', 'rb') as f: 
            strXml = f.read().decode('utf-8')
        parseData = ElementTree.fromstring(strXml) 
        
        elements = parseData.iter('row')
            
        i = 1
        for item in elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            SCHOOL_DIV = item.find('SCHOOL_DIV_NM')
            if InputLabel.get() not in part_el.text or School_text not in SCHOOL_DIV.text: 
                continue 
        
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text)
            listBox.insert(i-1, _text)
            i = i+1
    else:
        with open('project/xml/전문및대학교현황.xml', 'rb') as f: 
            strXml = f.read().decode('utf-8')
        parseData = ElementTree.fromstring(strXml) 
        
        elements = parseData.iter('row')

        i = 1
        for item in elements: # " row“ element들
            part_el = item.find('SIGUN_NM')
            if InputLabel.get() not in part_el.text: 
                continue 
        
            _text = '[' + str(i) + '] ' + \
                getStr(item.find('FACLT_NM').text) + \
                ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text)
            listBox.insert(i-1, _text)
            i = i+1



InitScreen()
g_Tk.mainloop()