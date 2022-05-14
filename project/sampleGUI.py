from tkinter import *
from tkinter import font
g_Tk = Tk()
g_Tk.geometry("400x600+450+100") # {width}x{height}+-{xpos}+-{ypos}
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
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#fbffdc')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#fbffdc')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, pady=10, bg='#fbffdc')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#fbffdc')
    frameList.pack(side="bottom", fill="both", expand=True)

    # title 부분
    MainText = Label(frameTitle, font = fontTitle, text="학교종이 땡땡땡")
    MainText.pack(anchor="center", fill="both")

    # 종류 선택 부분
    global SearchListBox 
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo, \
        font=fontNormal, activestyle='none', width=10, height=1, borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set) 
    slist = ["초등학교", "중학교", "고등학교", "대학교"]
    for i, s in enumerate(slist): 
        SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', padx=10, expand=True, fill="both")
    
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview) 
    
    sendEmailButton = Button(frameCombo, font = fontNormal, text='이메일') 
    sendEmailButton.pack(side='right', padx=10, fill='y')

    # 사용자 입력 부분
    global InputLabel
    InputLabel = Entry(frameEntry, font = fontNormal,width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack(side="left", padx=10, expand=True)

    SearchButton = Button(frameEntry, font = fontNormal, \
    text="검색", command=onSearch)
    SearchButton.pack(side="right", padx=10, expand=True, fill='y')

    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
        font=fontNormal, width=10, height=15, \
        borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set, bg='#eeffe6',selectbackground='#7ea26c')
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    
    LBScrollbar.pack(side="right", fill='y')
    LBScrollbar.config(command=listBox.yview)

def onSearch(): # "검색" 버튼 이벤트처리
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary() 
    elif iSearchIndex == 1: 
        pass 
    elif iSearchIndex == 2: 
        pass 
    elif iSearchIndex == 3:
        pass

def getStr(s): 
    return '' if not s else s

def SearchLibrary(): # "검색" 버튼 -> "도서관"
    from xml.etree import ElementTree 
    
    global listBox
    listBox.delete(0,listBox.size()) 
    
    with open('project/xml/초중고등학교현황.xml', 'rb') as f: 
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