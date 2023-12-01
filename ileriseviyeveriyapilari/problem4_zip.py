
isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

isimsoyisim = list(zip(isim,soyisim))

isimsoyisim.sort()

for i,j in isimsoyisim:
    print(i,j)