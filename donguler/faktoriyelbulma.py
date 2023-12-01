print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program Sonlandırılıyor.")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            print("Faktoriyel",faktoriyel,"i",i)
            faktoriyel *= i
        print(faktoriyel)
    break
