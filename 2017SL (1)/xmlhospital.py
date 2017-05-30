from xml.etree.ElementTree import parse
from xml.etree import ElementTree
import xml.etree.ElementTree as etree
import urllib
import urllib.request
import re
import http.client

##### global
xmlFD = -1
HospitalDoc = None
root = None
item_tag = None
sortType = 'nameup'
list = []
#tree = parse("hospital.xml")
#root = tree.getroot()
#item_tag = root.find("item")
#for country in root.iter("item"):
#    print ("=" * 60)

    # country의 child "rank" 출력
#    print ("Name : ", country.findtext("dutyName"))
    # country의 child "year" 출력
#    print("TellNum : ", country.findtext("dutyTel1"))


class GetData:
    key = 'fDs8VW%2BvtwQA8Q9LhBW%2BT2ETVBWWJaITjKfpzDsNJO8ugDsvdboInI16ZD295Txxtxwhc4G3PwMAvxd%2FWvz2gQ%3D%3D&pageNo=1&numOfRows=999'
    url = "http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?serviceKey=" + key

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        print(data)
        f = open("hospital.xml", "wb")
        f.write(data)
        f.close()

getData = GetData()
getData.main()

def HospitalFree():
    if checkDocument():
        HospitalDoc.unlink()

def checkDocument():
    global HospitalDoc
    if HospitalDoc == None:
        print("Error : Document is empty")
        return False
    return True

def PrintHospitalList():
    tree = etree.parse('hospital.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        InsertList(hospital)
    Sort()

def SearchHospitalAddr(keyword):
    tree = etree.parse('hospital.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        addr = str(hospital.findtext("dutyAddr"))
        if (addr.count(keyword) > 0):
            InsertList(hospital)
    Sort()

def SearchHospitalSubj(keyword):
    tree = etree.parse('hospital.xml')
    root = tree.getroot()
    DelList()

    for hospital in root.iter("item"):
        addr = str(hospital.findtext("dgidIdName"))
        if (addr.count(keyword) > 0):
            InsertList(hospital)
    Sort()


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
    dic= {'Name' : '', 'TellNum' : '', 'Subject' : '', 'Address' : ''}
    dic['Name'] = val.findtext("dutyName")
    dic['TellNum'] = val.findtext("dutyTel1")
    dic['Subject'] = val.findtext("dgidIdName")
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

def SortSel():
    global sortType
    print("now sortType : ", sortType)
    sortType = str(input('input new sortType(nameup, namedown, addrup, addrdown) :'))

def SortNameUp():
    global list
    i = 0
    while(i < len(list)):
        j = 0
        while (j < len(list)):
            if list[i]['Name'] < list[j]['Name']:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1

def SortNameDown():
    global list
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

def SortAddrUp():
    global list
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

def SortAddrDown():
    global list
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