

class tasit():

    def __init__(self,marka,hiz,teker_sayisi,motorlu,arac_durum = "Çalışmıyor"):

        self.marka = marka

        self.hiz = hiz

        self.teker_sayisi = teker_sayisi

        self.motorlu = motorlu

        self.arac_durum = arac_durum

    def start(self):
        self.arac_durum = "Çalışıyor"
        print("Taşıt Çalışıyor")

    def stop(self):
        self.arac_durum = "Çalışmıyor"
        print("Taşıt Çalışmıyor")

    def tasit_bilgi(self):

        print("Tasıt Sınıf Bilgileri:")
        print("{} Markalı Aracın Hızı {}\nteker sayısı {}\nmotor bilgisi {}\nArac durum {}".format(self.marka,self.hiz,self.teker_sayisi,self.motorlu,self.arac_durum))

"""
taşıt1 = tasit("BMW",100,4,True)

taşıt1.tasit_bilgi()
"""

class Otomobil(tasit):

    def __init__(self,marka,hiz,teker_sayisi,motorlu,arac_durum,beygir_gucu):
        super().__init__(marka,hiz,teker_sayisi,motorlu,arac_durum)

        print("Otomobil sınıfı init fonksiyonu")

        self.beygir_gucu = beygir_gucu

    def start(self):
        self.arac_durum = "Çalışıyor"
        print("Taşıt Çalışıyor")

    def stop(self):
        self.arac_durum = "Çalışmıyor"
        print("Taşıt Çalışmıyor")

    def beygir_arttır(self,beygir_miktarı):

        self.beygir_gucu += beygir_miktarı

    def tasit_bilgi(self):

        print("Otomobil Sınıf Bilgileri:")
        print("{} Markalı Aracın Hızı {}\nteker sayısı {}\nmotor bilgisi {}\nArac durum {}\nBeygir gücü {}".format(self.marka,self.hiz,self.teker_sayisi,self.motorlu,self.arac_durum,self.beygir_gucu))

"""
otomobil1 = Otomobil("Audi",80,4,True,"Çalışıyor",200)

otomobil1.tasit_bilgi()
"""

class Bisiklet(tasit):

    def __init__(self):