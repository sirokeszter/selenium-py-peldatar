# 2.	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
text = open('adat.txt', 'r')

mod_list = []
count = 1
for line in text:
    line = line.rstrip()
    mod_list.append(line)
    count += 1
print(mod_list)
