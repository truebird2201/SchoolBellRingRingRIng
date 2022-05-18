from tkinter import *
from tkinter import font
from tkinter import ttk
from xml.etree import ElementTree

g_Tk = Tk()
img = PhotoImage(file='image/Title.png')
img1 = PhotoImage(file='image/Search.png')
img2 = PhotoImage(file='image/BookMark.png')
img3 = PhotoImage(file='image/map.png')
def event_for_listbox(event): # 리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)


def InitScreen(): 
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
    frameResult = Frame(g_Tk, padx=10, pady=10, bg='#fffbd2')
    frameResult.pack(side="bottom", fill="both", expand=True)

    # title 부분

    titleimg = Label(frameTitle,image=img,bg='#fffbd2',text="초등학교")
    titleimg.pack(fill="both",expand=True, anchor = "center")

    # 종류 선택 부분
    radioValue = IntVar()
    global rcheck
    rcheck = 0
    r1 = Radiobutton(frameCombo, font=fontNormal, value=0, variable=radioValue, text="초등학교", command=lambda:CheckRadio(0), bg='#fff0f6') 
    r1.pack(side='left',expand=True, fill="both")
    
    r2 = Radiobutton(frameCombo, font=fontNormal, value=1, variable=radioValue, text="중학교", command=lambda:CheckRadio(1), bg='#fff0f6') 
    r2.pack(side='left',expand=True, fill="both")

    r3 = Radiobutton(frameCombo, font=fontNormal, value=2, variable=radioValue, text="고등학교", command=lambda:CheckRadio(2), bg='#fff0f6') 
    r3.pack(side='left',expand=True, fill="both")

    r4 = Radiobutton(frameCombo, font=fontNormal, value=3, variable=radioValue, text="대학교/대학원", command=lambda:CheckRadio(3), bg='#fff0f6') 
    r4.pack(side='left',expand=True, fill="both")
    

    # 사용자 입력 부분
    global InputLabel
    InputLabel = Entry(frameEntry, fg ='#ffaa00',selectbackground = "#ff6010",bg='White',
    insertbackground = '#ff6010',font = fontNormal,width = 30, borderwidth = 5, relief = 'sunken')
    InputLabel.pack(side="left", padx=10, expand=True)

    SearchButton = Button(frameEntry, font = fontNormal, \
    text="검색", command=onSearch,image=img1,)
    SearchButton.pack(side="right", expand=True)

    # 버튼 3개
    global LocalCombo
    Local_str = ['모두']
    Local_List_add(Local_str)
    LocalCombo = ttk.Combobox(framebotton,justify = 'center',foreground="#ffaa00",font=fontin, values = Local_str)
    LocalCombo.pack(side="left", padx=12,expand=True, fill='both')
    LocalCombo.set("모두")
    
    SearchButton = Button(framebotton, font = fontNormal,image=img3,  width = 100,text="지도")
    SearchButton.pack(side="right", padx=5, fill='both')
    SearchButton = Button(framebotton, font = fontNormal,image=img2,  width = 100,text="북마크",command=OnBookMark)
    SearchButton.pack(side="right", padx=5, fill='both')


    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameResult)
    listBox = Listbox(frameResult, selectmode='extended',fg ='#ff7b9e',selectforeground='White',selectbackground = "#ff7b9e",
        font=fontNormal, width=20, height=15, bg= '#fff0f6',\
        borderwidth=2, relief='ridge', yscrollcommand=LBScrollbar.set)
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
    global listBox, LocalCombo
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
                getStr(item.find('FACLT_NM').text) + \
                ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text)
            listBox.insert(i-1, _text)
            i = i+1
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
                getStr(item.find('FACLT_NM').text) + \
                ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text)
            listBox.insert(i-1, _text)
            i = i+1

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