
1. School_Bell_Ring.py	( 프로그램 실행 소스 )

  def event_for_listbox(event)
    - 리스트 선택 시 내용 출력
  def event_for_BookMarklistbox(event)
    - 북마크리스트 선택 시 내용 출력
  def InitScreen()
    - 화면그리기
  def drawGraph(canvas,data,canvasWidth,canvasHeight):
    - 그래프 그리기
  def CheckRadio(num):
    - 라디오버튼 처리
  def onSearch():
    - "검색" 버튼 이벤트처리
  def OnBookMark():
    - 북마크 팝업 설정 후 띄우기  
  def Clear(): 
    - 북마크 초기화
  def AddBookMark(botton ,name):
    - 북마크 추가
  def OnSchool(name):
    - 학교 팝업 설정 후 띄우기
  def OnMail(name):
    - 메일 보내기 팝업 설정 후 띄우기
  def SendMail(fromAddr,toAddr,msg):
    - 메일 보내기
  def OnMap():
    - 지도 팝업 설정 후 띄우기
  def onSearch_Map():
    - 지도 검색
  def getStr(s):
    - 문자열로 만들기
  def SearchLibrary(chk, onMap=False): 
    - 각종 검색을 위한 함수
  def Local_List_add(locallist):
    - 지역 별로 학교나누기
  def AddInformation(list, name):
    - 학교 상세 정보 추가

2. setup.py ( 배포판 생성 )

  spam모듈, 이미지들, xml파일, 텔레그램 모듈들을 배포판으로 묶음

3. teller.py ( 텔레그램 메인모듈 )

  def replyAptData(date_param, user, loc_param='대학', comm ='지역'):
    - 요청에 대한 대답
  def save( ser, loc_param ):
    - 정보 저장
  def check( user ):
    - 저장 정보 확인
  def handle(msg):
    - 텔레그램 핸들

4. noti.py ( 데이터 정보 )

  def getData(date_param , loc_param,  comm):
    - 정보 불러오기
  def sendMessage(user, msg):
    - 메세지 보내기

5. spammodule.c ( 스팸 모듈 )

  spam_strlen (PyObject* self, PyObject* args) -> 문자열 길이

6. BookMark.txt ( 북마크 내용 )

  북마크 내용을 binary형태로 저장 ( Pickle 모듈 사용 )