import time


class Pc():

    def __init__(self,pc_durum = "Kapalı",pc_dosyalar = ["Masaüstü","Dosyalar","Denetim Masası"],dosya = "Masaüstü"):

        self.pc_durum = pc_durum

        self.pc_dosyalar = pc_dosyalar

        self.dosya = dosya

    def pc_ac(self):

        if (self.pc_durum == "Kapalı"):

            self.pc_durum = "Açık"
            print("PC Acılıyor..")
            time.sleep(2)
            print("PC Açık",self.pc_durum)
        else:
            print("PC zaten açık")

    def pc_kapat(self):

        if (self.pc_durum == "Açık"):

            self.pc_durum = "Kapalı"
            print("PC Kapanıyor..")
            time.sleep(2)
        else:
            print("PC zaten kapalı")

    def dosya_ekle(self,dosya_ismi):

        self.pc_dosyalar.append(dosya_ismi)

    def dosya_sil(self,dosya_ismi1):

        self.pc_dosyalar.remove(dosya_ismi1)


    def __len__(self):

        return len(self.pc_dosyalar)

    def __str__(self):

        return "Pc Durumu: {}\nDosyalar: {}\nAçık Dosya: {}".format(self.pc_durum,self.pc_dosyalar,self.dosya)


pc = Pc()

print("""

PC Uygulaması

1. Pc Aç

2. Pc Kapat

3. Dosya Listesi

4. Dosya Ekle

5. Dosya Silme

""")

while True:
    islem = input("İşlem Seçiniz:")

    if (islem == "1"):
        if (pc.pc_durum == "Açık"):
            print("PC Açık")
        else:
            pc.pc_ac()

    elif (islem == "2"):
        if (pc.pc_durum == "Kapalı"):
            print("PC Kapalı")
        else:
            pc.pc_kapat()
            break

    elif (islem == "3"):
        if (pc.pc_durum == "Kapalı"):
            print("PC Aç")
        else:
            print(pc.pc_dosyalar)

    elif (islem == "4"):
        if (pc.pc_durum == "Kapalı"):
            print("PC Aç")
        else:
            dosya_isimleri = input("Dosya isimlerini ',' ile ayırarak girin:")

            dosya_listesi = dosya_isimleri.split(",")

            for eklenecekler in dosya_listesi:
                if eklenecekler in pc.pc_dosyalar:
                    print("{} dosyası zaten mevcut.".format(eklenecekler))
                else:
                    pc.dosya_ekle(eklenecekler)
                    print("{} dosyası eklendi.".format(eklenecekler))


    elif (islem == "5"):
        if (pc.pc_durum == "Kapalı"):
            print("PC Aç")
        else:
            dosya_isimleri = input("Dosya isimlerini ',' ile ayırarak girin:")

            dosya_listesi = dosya_isimleri.split(",")

            for silinecekler in dosya_listesi:
                if silinecekler in pc.pc_dosyalar:
                    pc.dosya_sil(silinecekler)
                    print("'{}' dosyası silindi.".format(silinecekler))
                else:
                    print("'{}' böyle bir dosya zaten yok".format(silinecekler))

    else:
        print("Hatalı İşlem Numarası")


