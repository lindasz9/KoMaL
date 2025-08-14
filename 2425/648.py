max, huzasok_szama = map(int, input("").split())

sorozat = []

for d in range(max):
    sorozat.append(d+1)

reszletek = []

for a in range(huzasok_szama):
    reszlet = list(map(int, input("").split()))
    reszletek.append(reszlet)

reszlet_szamai = []
szakaszok_szama = 1
legtobb_szakasz = 1
kihuzasok = 0
kihuzas = 1

for b in reszletek:
    kihuzasok += 1
    c = 0
    while c != (b[1] - b[0] + 1):
        reszlet_szamai.append(b[0]+c)
        c += 1
    if reszlet_szamai[0] != 1:
        if reszlet_szamai[-1] != max:
            if sorozat[reszlet_szamai[0] - 2] != 0:
                if sorozat[reszlet_szamai[-1]] != 0:
                    szakaszok_szama += 1
    if reszlet_szamai[0] == 1:
        if reszlet_szamai[-1] == max:
            szakaszok_szama -= 1
    if reszlet_szamai[0] != 1:
        if reszlet_szamai[-1] != max:
            if sorozat[reszlet_szamai[0] - 2] == 0:
                if sorozat[reszlet_szamai[-1]] == 0:
                    szakaszok_szama -= 1
    if szakaszok_szama > legtobb_szakasz:
        legtobb_szakasz = szakaszok_szama
        kihuzas = kihuzasok
    for e in reszlet_szamai:
        sorozat[sorozat.index(e)] = 0
    reszlet_szamai.clear()

print(kihuzas,legtobb_szakasz)