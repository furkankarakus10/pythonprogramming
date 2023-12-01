
with open("p1.txt","r",encoding="utf-8") as file:

    cumle = file.read()

    i = 0

    harfler = list()

    while i < len(cumle):

        harfler.append(cumle[i])

        i += 1

    print(harfler)
    print(type(harfler))




    harfler_kumesi = set()

    for i in harfler:

        harfler_kumesi.add(i)

    print(harfler_kumesi)
    print(type(harfler_kumesi))



    harf_sozluk = dict()

    for i in harfler:
        if (i in harf_sozluk):
            harf_sozluk[i] += 1
        else:
            harf_sozluk[i] = 1

    print(harf_sozluk.items())


    for harf,sayi in harf_sozluk.items():

        print("{} {}".format(harf, sayi))






