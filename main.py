liczbaDok = int(input())
dokumenty = []

for x in range(liczbaDok):
    a = input()
    dokumenty.append(a)

liczbaZapytan = int(input())
zapytania = []

for x in range(liczbaZapytan):
    b = input()
    zapytania.append(b)

for zapytanie in zapytania:
    slownik = {}
    for num, dok in enumerate(dokumenty):
        tokeny = dok.lower().split()
        if zapytanie in tokeny:
            slownik[num] = tokeny.count(zapytanie)
    print([w for w in sorted(slownik, key = slownik.get, reverse = True)])
