print(""""
*******************************
ATM

İşlemler;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için q ya basın
*******************************
""")

bakiye = 1000

while True:
    islem = input("İşlem Seçiniz:")
    if (islem == "q"):
        break
    elif (islem == "1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif (islem == "2"):
        miktar = int(input("Miktarı giriniz:"))
        bakiye += miktar
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if (bakiye - miktar < 0):
            print("Belirtilen miktarda bakiye bulunmamaktadır.")
            print("Bakiyeniz {} tldir".format(bakiye))
            continue
        bakiye -= miktar
    else:
        print("Geçersiz İşlem....")