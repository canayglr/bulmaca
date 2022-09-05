import json
from urllib.request import urlopen
from random import randint
bilmeceurl="https://raw.githubusercontent.com/canayglr/json/main/bilmeceler.json"
deger=urlopen(bilmeceurl).read().decode("utf-8")
jsonoku=json.loads(deger)
sayi=randint(0,7)
getdata=jsonoku["Bilmeceler"]
print(getdata[sayi]["b"] + " Bilmecesinin Cevabı "+ getdata[sayi]["c"])
cevap=input(getdata[sayi]["b"] + "\n")
if cevap==getdata[sayi]["c"]:
    print("Doğru Cevap!")
else:
    print("Cevap Yanlış!")
