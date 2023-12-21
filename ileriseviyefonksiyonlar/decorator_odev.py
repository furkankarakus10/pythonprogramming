def ekstra(fonk):

    def ekstra_ozellik(sayilar):
        print("Mükemmel Sayılar")
        for sayi in sayilar:
            toplam = 0
            i = 1
            while (i<sayi):
                if (sayi % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayi):
                print(sayi)

        fonk(sayilar)

    return ekstra_ozellik



@ekstra
def asalsayilar(sayilar):

    print("Asal Sayılar...")

    for sayi in sayilar:

        i = 2

        say = 0

        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1

        if (say == 0):
            print(sayi)

asalsayilar([1,2,3,4,5,6,7,8,9,10,11,12,13,14])