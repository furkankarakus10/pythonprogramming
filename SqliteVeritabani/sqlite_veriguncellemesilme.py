import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    con.commit()


def deger_ekle(isim, yazar, yayınevi, sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)", (isim, yazar, yayınevi, sayfa_sayısı))
    con.commit()


def verigüncelle(yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi =  ?", ("Everest", yayınevi))
    con.commit()


def verilerisil(yazar):
    cursor.execute("Delete  From kitaplık where Yazar = ?", (yazar,))
    con.commit()

verigüncelle("Doğan Kitap")
verilerisil("Ahmet Ümit")
con.close()