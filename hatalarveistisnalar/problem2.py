

liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def ciftmi(i):
        if (i % 2 == 0):
            return i
        else:
            raise ValueError("{} Tek Sayı".format(i))

for i in liste:
    try:
        print(ciftmi(i))
    except ValueError:
        pass




