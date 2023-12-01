print("""
*************************
1'den 1000'e kadar olan mükemmler sayılar
*************************
""")

def mukemmelsayi(sayi):
    tambolenler = []
    for i in range(1,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
            if (sum(tambolenler) == sayi):
                return True

for i in range(1,1000):
    if (mukemmelsayi(i)):
        print(i)

