from datetime import datetime

print(datetime.now())

su_an = datetime.now()

print(su_an.year)
print(su_an.month)
print(datetime.strftime(su_an,"%A"))

tarih = datetime(2023,9,25)

print(tarih)