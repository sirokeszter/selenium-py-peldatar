# Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t ami csak az emailím és név oszlopokat tartalmazza.
import csv

with open('table_in.csv', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(",".join(row[0:2]))