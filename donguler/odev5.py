print("""
**************************
3'e bölünen sayılar
**************************
""")

for i in range(1,101):
    if (i % 3 != 0):
            continue
    print(i)
