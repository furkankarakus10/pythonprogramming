print("""
**************************
Armstrong Sayı
**************************
""")

sayi = int(input("Sayı:"))
toplam = 0
rakamlar = [int(rakam) for rakam in str(sayi)]
print(rakamlar)

if (len(rakamlar) == 4):
    for i in rakamlar:
        toplam += i**4

    if (toplam == sayi):
        print("Armstrong Sayıdır.")
    else:
        print("Armstrong Sayı değildir.")
else:
    print("Dört basamaklı sayı giriniz...")