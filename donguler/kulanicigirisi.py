print(""""
*******************************
Kullanıcı Grişi Progarmı
*******************************
""")

sys_kullanici_adi = "ffurkan"

sys_parola = "12345"

giris_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı Adı Hatalı")
        giris_hakki -= 1
        print("Kalan giriş hakkı = {}".format(giris_hakki))
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola Hatalı")
        giris_hakki -= 1
        print("Kalan giriş hakkı = {}".format(giris_hakki))
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı")
        giris_hakki -= 1
        print("Kalan giriş hakkı = {}".format(giris_hakki))
    else:
        print("Sisteme Başarıyla giriş yapıldı")
        break
    if (giris_hakki == 0):
        print("giriş hakkınız kalmadı")
        break
