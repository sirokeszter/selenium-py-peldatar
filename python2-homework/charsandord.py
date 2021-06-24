import string

text = open("text.txt", "r")

dictionary = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")

    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1

for key in list(dictionary.keys()):
    print(key, dictionary[key])

# Egy neten talált példa alapján dolgoztam, kiszedve az írásjeleket is. Egy dolgot nem tudtam megoldani,maradt benne egy olyan sor, ahol üres elemeket talált meg 9x.