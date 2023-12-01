print("""
dikdörtgenin eknarları(dk) alanını veren liste

çözüm:

def alan_hesapla(demet):
    return demet[0] * demet[1]


liste = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan_hesapla,liste)))


""")


dk = [(3,4),(10,3),(5,6),(1,9)]

def aa(x):
    a = []
    b = []

    for i in x:
        for index,eleman in enumerate(i):
            if (index % 2 == 0):
                a.append(eleman)
            else:
                b.append(eleman)

    c = list(map(lambda x,y : x * y ,a,b))

    return c

print(aa(dk))