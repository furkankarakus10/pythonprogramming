print("""*******************
Fibonacci Serisi

*******************""")

while True:

    liste = [1,1]
    for i in range(10):
        a = liste[-1] + liste[-2]
        liste.append(a)

    print(liste)
    break

