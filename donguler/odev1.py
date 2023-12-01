print("""
**************************
Mükemmel Sayı
**************************
""")

sayi = int(input("Sayı:"))
toplam = 0

for i in range(1,sayi-1):
        if (sayi % i == 0):
            toplam += i
            i += 1
if (toplam == sayi):
    print("mükemmel sayıdır")
else:
    print("mükemmel sayı değildir")
