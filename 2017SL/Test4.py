import smtplib
import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import xml.etree.ElementTree as etree

mailList = []
sortType = "nameup"

def sendMail():
    host = "smtp.gmail.com"
    port = "587"
    html = ""
    title = input("title")
    sendID = input("send id")
    reciveID = input("recive id")
    msgtext = input("messge")
    passwd = input("password")
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
    global mailList
    tree = etree.parse('sample.xml')
    root = tree.getroot()
    mailList = []

    for hospital in root.iter("item"):
        InsertList(hospital)
    Sort()
    return mailList

def InsertList(val):
    global mailList
    dic = {'Name': '', 'TellNum': '', 'Subject': '', 'Address': ''}
    dic['Name'] = val.findtext("dutyName")
    dic['TellNum'] = val.findtext("dutyTel1")
    dic['Subject'] = val.findtext("dgidIdName")
    dic['Address'] = val.findtext("dutyAddr")

    mailList.append(dic)

def Sort():
    global mailList, sortType

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

def SortNameUp():
    global mailList,List1
    temp = 1
    i = 0
    while(i < len(mailList)):
        j = 0
        while (j < len(mailList)):
            if mailList[i]['Name'] < mailList[j]['Name']:
                temp = mailList[i]
                mailList[i] = mailList[j]
                mailList[j] = temp
            j += 1
        i += 1

def SortNameDown():
    global mailList,List1
    temp = 1
    i = 0
    while (i < len(mailList)):
        j = 0
        while (j < len(mailList)):
            if mailList[i]['Name'] > mailList[j]['Name']:
                temp = mailList[i]
                mailList[i] = mailList[j]
                mailList[j] = temp
            j += 1
        i += 1

def SortAddrUp():
    global mailList,List1
    temp = 1
    i = 0
    while (i < len(mailList)):
        j = 0
        while (j < len(mailList)):
            if mailList[i]['Address'] < mailList[j]['Address']:
                temp = mailList[i]
                mailList[i] = mailList[j]
                mailList[j] = temp
            j += 1
        i += 1

def SortAddrDown():
    global mailList,List1
    temp = 1
    i = 0
    while (i < len(mailList)):
        j = 0
        while (j < len(mailList)):
            if mailList[i]['Address'] > mailList[j]['Address']:
                temp = mailList[i]
                mailList[i] = mailList[j]
                mailList[j] = temp
            j += 1
        i += 1


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
        ibsnText = newdoc.createTextNode("Name:" + item['Name'])
        b.appendChild(ibsnText)

        body.appendChild(b)

        # BR 태그 (엘리먼트) 생성.
        br = newdoc.createElement('br')

        body.appendChild(br)

        # create title Element
        p = newdoc.createElement('p')
        # create text node
        titleText = newdoc.createTextNode("Address:" + item['Address'])
        p.appendChild(titleText)

        body.appendChild(p)
        body.appendChild(br)  # line end

        # append Body
    top_element.appendChild(body)

    return newdoc.toxml()

sendMail()