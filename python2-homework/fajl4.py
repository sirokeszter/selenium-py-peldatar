# 4.	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így, ahogy beolvastad, soronként egy szóval egy másik fájlba!

text = open('adat.txt', 'r')

mod_list = []
count = 1
for line in text:
    line = line.rstrip()
    mod_list.append(line)
    count += 1
print(mod_list)

print("-" * 30)

# új fájlban kiírva:

new_text = '\n'.join(mod_list)
print(new_text)
