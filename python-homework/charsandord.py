sor1=list(range(97,107))
sor2=list(range(107,118))
sor3=list(range(118,129))

for i in range(0,len(sor1)):
    print(chr(sor1[i]),sor1[i],chr(sor2[i]),sor2[i],chr(sor3[i]),sor3[i])

print("*"*20) # elválasztásképpen

# Másik megoldás:
my_list=[97,107,118]
for i in range(10):
  print(my_list[0] +i, chr(my_list[0] +i), my_list[1] +i, chr(my_list[1] +i), my_list[2] +i, chr(my_list[2] +i))


print("*"*20)

# A második megoldás erősen "megerőszakolva", hogy csak a kisbetűket írja ki. Ennél biztos van szebb megoldás is, de ez legalább működik :-)

my_list=[97,107,118]
for i in range(5):
  print(my_list[0] +i, chr(my_list[0] +i), my_list[1] +i, chr(my_list[1] +i), my_list[2] +i, chr(my_list[2] +i))
my_list=[102,112]
for i in range(5):
  print(my_list[0] +i, chr(my_list[0] +i), my_list[1] +i, chr(my_list[1] +i))