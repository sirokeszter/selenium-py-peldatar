text = open('adat.txt', 'r')

mod_list = []
count = 1
for line in text:
    line = line.rstrip()
    mod_list.append(line)
    count += 1
print(mod_list)

text_inline = ' '.join(mod_list)
print(text_inline)