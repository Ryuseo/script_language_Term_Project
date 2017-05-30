import os
import sys
import urllib.request
import xml.etree.ElementTree as etree
import webbrowser
import json
client_id = "lDQGy6423r9gVPB7peM1"
client_secret = "JPWnUvmmBh"
encText = urllib.parse.quote("인천광역시 계양구 계양문화로 20")
#url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
#url = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=lDQGy6423r9gVPB7peM1&url=http://naver.com&crs=EPSG:4326&center=126.7368531,37.5325394&level=10&w=800&h=640&baselayer=default"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #webbrowser.open(url)
    test = response_body.decode('utf-8')
    #print(test)
    #print(test.find('point'))
    test2 = json.loads(test)
    

else:
    print("Error Code:" + rescode)