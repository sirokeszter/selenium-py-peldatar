# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla.
# Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
# Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
# Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon, a kólája.")

kerdes1= input("Adja meg az életkorát! Válasz: ")
print(kerdes1)
kerdes2= input("Mit iszik? Válasz: ")
print(kerdes2)

if kerdes2 != "kóla" and kerdes2 != "sör":
    print("Csak sört és kólát tudunk adni")
else:
    print(" ")
if int(kerdes1) < 18 and kerdes2 == "sör":
    print("Kiskorúakat nem szolgáhatunk ki alkohollal!")
elif int(kerdes1) >= 18 and kerdes2 == "sör":
    print("Parancsoljon, a söre!")
else:
    print("")
if int(kerdes1) > 60 and kerdes2 == "kóla":
    print("A koffein emelheti a vérnyomását!")
elif int(kerdes1) >= 60 and kerdes2 == "kóla":
    print("Parancsoljon, a kólája")
else:
    print(" ")