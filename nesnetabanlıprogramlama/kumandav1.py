import random
import time

class Kumanda():


    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt",parlaklik = 50):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

        self.parlaklik = parlaklik

    def tv_ac(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tv_durum  = "Açık"

    def tv_kapat(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap =  input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : 'çıkış'\n :")

            if (cevap == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 31):

                    self.tv_ses += 1

                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi.....")
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)


        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:" ,self.kanal)

    def parlaklik_ayarları(self):

        while True:
            cevap1 =  input("Parlaklık Azalt: '-'\nParlaklık Artır: '+'\nGeri : 'x'\n :")

            if (cevap1 == "-"):
                if (self.parlaklik != 0):

                    self.parlaklik -= 1
                    print("Parlaklık:",self.parlaklik)
            elif (cevap1 == "+"):
                if (self.parlaklik != 100):

                    self.parlaklik += 1

                    print("Parlaklık:",self.parlaklik)
            else:
                print("Parlaklık Güncellendi:",self.parlaklik)
                break

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\nParlaklık: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal,self.parlaklik)


kumanda = Kumanda()


print("""

Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Parlaklık Ayarları

6. Kanal Sayısını Öğrenme

7. Rastgele Kanala Geçme

8. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")


while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()

    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        if (kumanda.tv_durum == "Açık"):
            kumanda.ses_ayarları()
        else:
            print("Tv Kapalı")

    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif (işlem == "5"):
        kumanda.parlaklik_ayarları()

    elif (işlem == "6"):

        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "7"):
        kumanda.rastgele_kanal()

    elif (işlem == "8"):
        print(kumanda)

    else:
        print("Geçersiz İşlem......")



