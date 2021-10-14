f = open("EUtagallamai.txt","r", encoding = "UTF-8")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
f.close()
statisztika = dict()
for sor in lista:
    ev = sor[1][:4]
    statisztika[ev] = statisztika.get(ev,0) + 1
for sor in statisztika.items():
    print(f"{sor[0]} - {sor[1]}")