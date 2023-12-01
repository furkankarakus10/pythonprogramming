
with open("mailler.txt","r",encoding="utf-8") as file:

    for i in file:
        i = i[:-1]
        if (i.endswith(".com") and i.find("@") != -1):
            print(i)


        """
        print(i)
        print(i.find("@"))
        print(i.endswith(".com"))
        """

        """
        if i.endswith(".com") == True and i.find("@") >= 0:
            print("mail",i)
        else:
            print("mail değil",i)
        """
