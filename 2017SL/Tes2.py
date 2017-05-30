import xml.etree.ElementTree as etree

def main():
    tree = etree.parse('sample.xml')
    root = tree.getroot()

    for hospital in root.iter("item"):
        test2 = str(hospital.findtext("dutyAddr"))
        if (test2.count('인천') > 0):
            print("=" * 60)
            print("Name : ", hospital.findtext("dutyName"))
            print("TellNum : ", hospital.findtext("dutyTel1"))


            print("Subject : ",  test2)
            print("Address : ", hospital.findtext("dutyAddr"))

if __name__ == "__main__":
    main()

