
with open("siir.txt","r",encoding="utf-8") as file:

    kelime = ""

    for i in file:
        i = i.strip()
        i = i[0]
        kelime = kelime+i

    print(kelime)

