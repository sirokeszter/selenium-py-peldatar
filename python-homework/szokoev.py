# •	Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik, nem szökőév minden századik, mégis az minden 400-adik.
# (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)


def szokoev(ev):
    if ev % 4 == 0:
        return True
    elif ev % 100 != 0 and ev % 400 ==0:
        return True
    else:
        return False

print (szokoev(2100))
