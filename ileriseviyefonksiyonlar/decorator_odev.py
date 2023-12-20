
def asalsayilar(sayilar):

    asalolan = []
    asalolmayanlar = []

    for sayi in sayilar:

        if (sayi == 1):

            asalolan.append(sayi)

        elif (sayi == 2):

            asalolmayanlar.append(sayi)

        else:

            for i in range(2,sayi):

                if (sayi % i != 0 ):

                    asalolan.append(sayi)
    print(asalolan)

    return asalolan

asalsayilar([1,2,3,4,5,6,7,8,9,10])
