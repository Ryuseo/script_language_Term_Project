loopFlag = 1
from internethospital import *


#### Menu  implementation
def printMenu():
    print("₩nWelcome! Hospital Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Quit program:   q")
    print("Print Hospital list: b")
    print("Search Hospital Addr: e")
    print("Search Hospital Addr: i")
    print("SortType select s")
    print("send maIl : j")
    print("========Menu==========")


def launcherFunction(menu):
    if menu == 'l':
        getData = GetData()
        getData.main()
    elif menu == 'q':
        QuitHospitalMgr()
    elif menu == 'b':
        PrintHospitalList()
    elif menu == 'e':
        keyword = str(input('input keyword to search :'))
        SearchHospitalAddr(keyword)
    elif menu == 'i':
        keyword = str(input('input keyword to search :'))
        SearchHospitalSubj(keyword)
    elif menu == 's':
        SortSel()
    else:
        print("error : unknow menu key")


def QuitHospitalMgr():
    global loopFlag
    loopFlag = 0
    HospitalFree()


##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")
