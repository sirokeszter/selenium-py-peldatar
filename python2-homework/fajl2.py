# 2.	Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!
text = open('adat.txt', 'r')
x = text.readlines()
print(x) # itt még le kellene vágni a lista elemeinél a töréspontokat
y = ''.join(x)
text_inline = y.replace('\n', ' ')
print(text_inline)