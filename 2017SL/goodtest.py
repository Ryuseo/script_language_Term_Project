from tkinter import *
from tkinter import font
import xml.etree.ElementTree as etree
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import urllib.request
import webbrowser
from io import BytesIO
#from PIL import Image,ImageTk
import io
import base64

mailList = []
mapValue = " "
client_id = "lDQGy6423r9gVPB7peM1"
client_secret = "JPWnUvmmBh"
def bind(widget, event):
   def decorator(func):
       widget.bind(event, func)
       return func

   return decorator









def UrlBuilder(xcode, ycode):
    url = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=lDQGy6423r9gVPB7peM1&url=http://naver.com&crs=EPSG:4326&center=" + xcode + ycode + "&level=10&w=400&h=320&baselayer=default"
    return url
def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.grid(row=0, column=5)
    RenderTextScrollbar.place(x=300, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=35, height=30, borderwidth=12, relief='ridge',
                      yscrollcommand=RenderTextScrollbar.set)
    RenderText.grid(row=3, column=0)
    RenderText.place(x=10, y=145)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.place(x=300, y=200)
    RenderText.configure(state='disabled')
def PrintHospitalList():
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        InsertList(hospital)
    Sort()
def SearchHospitalAddr():
    global list, list1, mapValue,client_id,client_secret
    temp = 1
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        addr = str(hospital.findtext("dutyAddr"))
        if (addr.count(SearchAddr.get()) > 0):
            InsertList(hospital)
    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)

    for i in list:
        list1.insert(temp, "========================================")
        temp += 1
        list1.insert(temp, i['Name'])
        temp += 1
        list1.insert(temp, i['TellNum'])
        temp += 1
        list1.insert(temp, i['Subject'])
        temp += 1
        list1.insert(temp, i['Address'])
        temp += 1

    list1.insert(temp, "========================================")

    def CurSelect(evt):
        global window, image_byt, image_b64, photo, label
        mapValue = str(list1.get(list1.curselection()))
        print(mapValue)
        encText = urllib.parse.quote(mapValue)
        print(encText)
        url = "https://openapi.naver.com/v1/map/geocode?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            # webbrowser.open(url)
            test = response_body.decode('utf-8')
            print(test)
            test2 = test.split()
            index1 = test.find("x")
            print(index1)
            url2 = UrlBuilder(test2[40],test2[42]) #광주 광역시
            print(test2[42],test2[44])
            # print(test['point'])
            # test2 = json.loads(test)


        else:
            print("Error Code:" + rescode)
        image_byt = urllib.request.urlopen(url2).read()
        image_b64 = base64.encodebytes(image_byt)
        photo = PhotoImage(data=image_b64)

        label = Label(window, image=photo, height=400, width=400)

        label.place(x=330, y=0)

    list1.bind('<<ListboxSelect>>', CurSelect)
    print(mapValue)


    # PrintList()
def SearchHospitalSubj():
    global list1
    temp = 1
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        addr = str(hospital.findtext("dgidIdName"))
        if (addr.count(SearchSub.get()) > 0):
            InsertList(hospital)

    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)
    for i in list:
        list1.insert(temp, "========================================")
        temp += 1
        list1.insert(temp, i['Name'])
        temp += 1
        list1.insert(temp, i['TellNum'])
        temp += 1
        list1.insert(temp, i['Subject'])
        temp += 1
        list1.insert(temp, i['Address'])
        temp += 1

    list1.insert(temp, "========================================")

    def CurSelect(evt):
        global window, image_byt, image_b64, photo, label
        mapValue = str(list1.get(list1.curselection()))
        print(mapValue)
        encText = urllib.parse.quote(mapValue)
        print(encText)
        url = "https://openapi.naver.com/v1/map/geocode?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            # webbrowser.open(url)
            test = response_body.decode('utf-8')
            print(test)
            test2 = test.split()
            index1 = test.find("x")
            print(index1)
            url2 = UrlBuilder(test2[42], test2[44])  # 광주 광역시
            print(test2[42], test2[44])
            # print(test['point'])
            # test2 = json.loads(test)


        else:
            print("Error Code:" + rescode)
        image_byt = urllib.request.urlopen(url2).read()
        image_b64 = base64.encodebytes(image_byt)
        photo = PhotoImage(data=image_b64)

        label = Label(window, image=photo, height=400, width=400)

        label.place(x=330, y=0)

    list1.bind('<<ListboxSelect>>', CurSelect)
    print(mapValue)
    PrintList()
def PrintList():
    global list

    for i in list:
        print("=" * 60)
        print("Name : ", i['Name'])
        print("TellNum : ", i['TellNum'])
        print("Subject : ", i['Subject'])
        print("Address : ", i['Address'])
def DelList():
    global list
    list = []
def InsertList(val):
    global list
    dic = {'Name': '', 'TellNum': '', 'Subject': '', 'Address': ''}
    dic['Name'] = val.findtext("dutyName")
    dic['TellNum'] = val.findtext("dutyTel1")
    dic['Subject'] = str(val.findtext("dgidIdName"))
    dic['Address'] = val.findtext("dutyAddr")

    list.append(dic)
def Sort():
    global list, sortType

    if sortType == 'nameup':
        SortNameUp()
    elif sortType == 'namedown':
        SortNameDown()
    elif sortType == 'addrup':
        SortAddrUp()
    elif sortType == 'addrdown':
        SortAddrDown()
    else:
        print("no sortType. restart SortSel")
    PrintList()
def SortNameUp():
    global list, list1
    temp = 1
    i = 0
    while (i < len(list)):
        j = 0
        while (j < len(list)):
            if list[i]['Name'] < list[j]['Name']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)
    for i in list:
        list1.insert(0, "========================================")

        list1.insert(0, i['Name'])

        list1.insert(0, i['TellNum'])

        list1.insert(0, i['Subject'])

        list1.insert(0, i['Address'])

    list1.insert(0, "========================================")
    PrintList()
def SortNameDown():
    global list, list1
    temp = 1
    i = 0
    while (i < len(list)):
        j = 0
        while (j < len(list)):
            if list[i]['Name'] > list[j]['Name']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)
    for i in list:
        list1.insert(0, "========================================")

        list1.insert(0, i['Name'])

        list1.insert(0, i['TellNum'])

        list1.insert(0, i['Subject'])

        list1.insert(0, i['Address'])

    list1.insert(0, "========================================")
    PrintList()
def SortAddrUp():
    global list, list1
    temp = 1
    i = 0
    while (i < len(list)):
        j = 0
        while (j < len(list)):
            if list[i]['Address'] < list[j]['Address']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)
    for i in list:
        list1.insert(0, "========================================")

        list1.insert(0, i['Name'])

        list1.insert(0, i['TellNum'])

        list1.insert(0, i['Subject'])

        list1.insert(0, i['Address'])

    list1.insert(0, "========================================")

    PrintList()
def SortAddrDown():
    global list, list1
    temp = 1
    i = 0
    while (i < len(list)):
        j = 0
        while (j < len(list)):
            if list[i]['Address'] > list[j]['Address']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    list1.delete(0, END)
    Scrollbar1 = Scrollbar(window)
    Scrollbar1.place(x=300, y=200)
    Scrollbar2 = Scrollbar(window)
    Scrollbar2.place(x=300, y=300)
    list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set)
    list1.place(x=10, y=145)
    Scrollbar1.config(command=list1.yview)
    Scrollbar2.config(command=list1.xview)
    for i in list:
        list1.insert(0, "========================================")

        list1.insert(0, i['Name'])

        list1.insert(0, i['TellNum'])

        list1.insert(0, i['Subject'])

        list1.insert(0, i['Address'])

    list1.insert(0, "========================================")
    PrintList()
def MakeHtmlDoc(list):
    from xml.dom.minidom import getDOMImplementation
    # get Dom Implementation
    impl = getDOMImplementation()

    newdoc = impl.createDocument(None, "html", None)  # DOM 객체 생성
    top_element = newdoc.documentElement
    header = newdoc.createElement('header')
    top_element.appendChild(header)

    # Body 엘리먼트 생성.
    body = newdoc.createElement('body')

    for item in list:
        # create bold element
        b = newdoc.createElement('b')
        # create text node
        nameText = newdoc.createTextNode("Name:" + item['Name'])
        b.appendChild(nameText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        #body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        addrText = newdoc.createTextNode("Address:" + item['Address'])
        p.appendChild(addrText)

        body.appendChild(p)
        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        subText = newdoc.createTextNode("Subject:" + item['Subject'])
        p.appendChild(subText)

        body.appendChild(p)
        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        telText = newdoc.createTextNode("TellNum:" + item['TellNum'])
        p.appendChild(telText)

        body.appendChild(p)

        # append Body
    top_element.appendChild(body)

    return newdoc.toxml()
def sendMail():
    host = "smtp.gmail.com"
    port = "587"
    html = ""
    title = "title"
    sendID = "rkd4apf@gmail.com"
    reciveID = "rkd4apf@gmail.com"
    msgtext = "messge"
    passwd = "momo8591!"
    html = MakeHtmlDoc(MakeList())

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = sendID
    msg['To'] = reciveID

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = smtplib.SMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sendID, passwd)  # 로긴을 합니다.
    s.sendmail(sendID, [reciveID], msg.as_string())
    s.close()

    print("Mail sending complete!!!")
def MakeList():
    global list
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    list = []

    for hospital in root.iter("item"):
        InsertList(hospital)
    Sort()
    return list

window = Tk()
window.geometry("750x600+200+200")
Title = Label(window, text='응급의료기관 검색', font='helvetica 16')
Title.grid(row=0, column=3)
TextSearchAddr = Label(window, text='주소검색')
TextSearchSub = Label(window, text='진료과목검색')
TextSearchAddr.grid(row=1, column=2)
TextSearchSub.grid(row=2, column=2)
SearchAddr = Entry(window)

SearchSub = Entry(window)
SearchAddr.grid(row=1, column=3)
SearchSub.grid(row=2, column=3)

Mailsender = Label(window, text='보내는사람')
Mailreciver = Label(window, text='받는사람')
password = Label(window, text='비밀번호')
Mailsender.place(x=330, y=400)
Mailreciver.place(x=330, y=425)
password.place(x=330, y=450)
Mailsender = Entry(window)
Mailreciver = Entry(window)
password = Entry(window)
Mailsender.place(x=400, y=400)
Mailreciver.place(x=400, y=425)
password.place(x=400, y=450)

b7 = Button(window, text="보내기", command=sendMail)
b7.place(x=550, y=425)

sortType = 'nameup'
list = []
Scrollbar1 = Scrollbar(window)
Scrollbar1.place(x=300, y=200)
Scrollbar2 = Scrollbar(window)
Scrollbar2.place(x=300, y=300)


b1 = Button(window, text="검색", command=SearchHospitalAddr)
b2 = Button(window, text="검색", command=SearchHospitalSubj)
b1.grid(row=1, column=4)
b2.grid(row=2, column=4)

b3 = Button(window, text="주소오름차순", command=SortAddrUp)
b4 = Button(window, text="주소내림차순", command=SortAddrDown)
b3.place(x=0, y=110)
b4.place(x=80, y=110)
b5 = Button(window, text="이름오름차순", command=SortNameUp)
b6 = Button(window, text="이름내림차순", command=SortNameDown)
b5.place(x=160, y=110)
b6.place(x=240, y=110)

encText = urllib.parse.quote("인천광역시 계양구 계양문화로 20 (작전동)")
print(encText)
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
#url = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=lDQGy6423r9gVPB7peM1&url=http://naver.com&crs=EPSG:4326&center=4126.7368531,37.532539&level=10&w=800&h=640&baselayer=default"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #webbrowser.open(url)
    test = response_body.decode('utf-8')
    print(test)
    test2 = test.split()
    url2 = UrlBuilder(test2[42],test2[44])
    print(test2[42],test2[44])
    #print(test['point'])
    # test2 = json.loads(test)
    #webbrowser.open(url2)

else:
    print("Error Code:" + rescode)

image_byt = urllib.request.urlopen(url2).read()
image_b64 = base64.encodebytes(image_byt)
photo = PhotoImage(data=image_b64)

label = Label(window, image=photo, height=400, width=400)

label.place(x=330, y=0)
list1 = Listbox(window, width=40, height=25, xscrollcommand=Scrollbar2.set, yscrollcommand=Scrollbar1.set,name='list1')

list1.place(x=10, y=145)
Scrollbar2.config(command=list1.xview)
Scrollbar1.config(command=list1.yview)






window.mainloop()