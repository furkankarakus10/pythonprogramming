print("""
*************************
Mukemmel Sayi mi ?
*************************
""")
def mukemmelsayi(sayi):
    tambolenler = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tambolenler.append(i)
            if (sum(tambolenler) == sayi):
                return True

while True:
    sayi = input("Sayı:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)

        if mukemmelsayi(sayi):
            print(sayi,"mükemmel sayıdır.")
        else:
            print(sayi,"mukemmel sayı degildir.")
