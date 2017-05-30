import urllib.request

class GetData:
    key = 'fDs8VW%2BvtwQA8Q9LhBW%2BT2ETVBWWJaITjKfpzDsNJO8ugDsvdboInI16ZD295Txxtxwhc4G3PwMAvxd%2FWvz2gQ%3D%3D&pageNo=1&numOfRows=999'
    url = "http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?serviceKey=" + key

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        print(data)
        f = open("sample.xml", "wb")
        f.write(data)
        f.close()

getData = GetData()
getData.main()
