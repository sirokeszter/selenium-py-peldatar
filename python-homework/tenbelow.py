szam=0
osszeg=0

while szam<10:
    szam=int(input())
    if int(szam>9):
        break
    osszeg += szam
print(osszeg)
