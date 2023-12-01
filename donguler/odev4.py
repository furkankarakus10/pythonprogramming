print("""
**************************
Problem 4
**************************
""")

toplam = 0

while True:
    sayi = input("Sayi:")
    if (sayi == "q"):
        print("program durduruldu.")
        break
    sayi = int(sayi)
    toplam += sayi
print(toplam)

