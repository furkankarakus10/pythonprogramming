print("""
*************************
Tam Bolen Bulma
*************************
tam_bolenler(int(input("Sayı:")))
""")

tambolenler = []

def tam_bolenler(sayi):
    for i in range(1,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
        i += 1
    print("{} sayısının tam bolenleri {}".format(sayi,tambolenler))

while True:
    sayi = input("Sayı:")

    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)
        tam_bolenler(sayi)