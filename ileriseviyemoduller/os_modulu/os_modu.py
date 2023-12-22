import os
from datetime import datetime

##print(dir(os))

"""
print("\n")
os.chdir("D:")
print(os.getcwd())
print("\n")
print(os.listdir())
for i in os.listdir():
    print(i)

print("\n")
print(os.getcwd())
##os.mkdir("Deneme1")
os.makedirs("Deneme2/Deneme3")

print("\n")
print(os.getcwd())
##os.rmdir("Deneme2/Deneme3")
##os.mkdir("Deneme2/Deneme3")
##os.removedirs("Deneme2/Deneme3")

print("\n")
print(os.getcwd())
#f = open("text.txt","x")
#f = open("text.txt","w")
#f.write("bu bir deneme dosyasıdır.")
#os.rename("text.txt","text2.txt")
#print(os.stat("text2.txt"))
print(datetime.fromtimestamp(os.stat("text2.txt").st_mtime))

print("\n")
print(os.walk("D:"))

for klasor_yolu,klasor_isimleri,dosya_isimler in os.walk("D:"):
    for i in klasor_isimleri:
        if (i.endswith(".txt")):
            print(i)
"""

print("\n")
print(os.getcwd())



















