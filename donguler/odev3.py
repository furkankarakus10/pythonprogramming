print("""
**************************
Çarpım Tablosu
**************************
""")

for i in range(1,11):
    for a in range(1,11):
        print("{} * {} = {}".format(i,a,i * a))
        a += 1
    print("-----------")
    i += 1