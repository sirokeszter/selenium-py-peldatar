# 1.	Olvasd be a fájlt, és írd ki a tartalmát egy sorba, úgy, hogy nem tárolod el a szöveget, hanem minden sort azonnal kiírsz!

with open('adat.txt') as text:
    print(' '.join([line.rstrip('\n') for line in text]))