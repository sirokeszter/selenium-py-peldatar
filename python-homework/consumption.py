print("külterületi út km-ben: ")
road_out = input()
print("városi út km-ben: ")
road_in = input()
print("külterületi fogyasztás literben: ")
cons_out = input()
print("városi fogyasztás literben: ")
cons_in = input() #belterületi fogyasztás
print("benzin ára Ft-ban: ")
fuel = input()

# Fogyasztás csak odaútra:

print(int(road_out)/int(100)*int(cons_out) + int(road_in)/int(100)*int(cons_in))

# Fogyasztás oda-vissza:

print((int(road_out)/int(100)*int(cons_out) + int(road_in)/int(100)*int(cons_in))*2)

# Teljes út ára:
print((int(road_out)/int(100)*int(cons_out) + int(road_in)/int(100)*int(cons_in))*2*int(fuel))