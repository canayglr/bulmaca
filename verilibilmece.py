import json
from urllib.request import urlopen
from random import randint
bilmeceurl="https://raw.githubusercontent.com/canayglr/bulmaca/main/bilmeceler.json"
deger=urlopen(bilmeceurl).read().decode("utf-8")
jsonoku=json.loads(deger)
getdata=jsonoku["Bilmeceler"]
hak=3
input("Bilmece oyununa hoşgeldiniz, 3 yanlış hakkınız var devam etmek için herhangi bir tuşa basınız!")
while True:
    if hak==0:
        print("Üzgünüm Dostum Elendiniz!")
        break
    else:
        sayi=randint(0,7)
        # print(getdata[sayi]["b"] + " Bilmecesinin Cevabı "+ getdata[sayi]["c"])
        cevap=input(getdata[sayi]["b"] + "\n")
        if cevap==getdata[sayi]["c"]:
            a=input("Soruyu doğru yanıtladınız çıkmak için [0] devam etmek için herhangi bir tuşa basınız.\n")
            if a=="0":
                print("Yarışma Sonlandırılmıştır!")
                break
                
        else:
            hak=hak-1
            print(f"Soruya yanlış cevap verdiniz {hak} hakkınız kaldı!")
