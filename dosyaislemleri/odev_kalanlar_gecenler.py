
def gecenler_kalanlar(satır):
    satır = satır[:-1]

    liste = satır.split("------------------> ")

    harf = liste[1]

    if (harf != 'FF'):

        liste.append('kaldı')
    else:

        liste.append('gecti')

    return liste





with open("notlar.txt","r",encoding="utf-8") as file:

    kalanlar_listesi = []

    gecenler_listesi = []

    for i in file:
        a = gecenler_kalanlar(i)
        isim = a[0]
        not_ = a[1]
        sonuc = a[2]

        if (a[2] == "kaldı"):

            kalanlar_listesi.append(a)

        else:

            gecenler_listesi.append(a)


with open("kalanlar.txt","w",encoding="utf-8") as file2:

    for i in kalanlar_listesi:
        file2.write(i[0]+","+i[1]+","+i[2]+"\n")

with open("gecenler.txt", "w", encoding="utf-8") as file3:

    for i in gecenler_listesi:
        file3.write(i[0]+","+i[1]+","+i[2]+"\n")

"""
    print("kalanlar listesi\n")
    print(kalanlar_listesi)
    print("geçenler listesi\n")
    print(gecenler_listesi)
"""










