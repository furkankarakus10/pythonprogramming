print("""
*************************
İki basamaklı Sayının Okunuşu
*************************
""")

birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı):
    birinci = sayı % 10
    print(birinci)
    ikinci = sayı // 10
    print(ikinci)

    return onlar[ikinci] + " " + birler[birinci]


sayı = int(input("Sayı:"))

print(okunus(sayı))