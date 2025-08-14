jatekok = int(input(""))
gyoztesek_input = input("")
gyoztesek = list(map(int, gyoztesek_input.split()))

szakasz = []
szakasz_vissza = []
harom_kulonbozo = []
ketto_kulonbozo = []
legtobb_elem = 0
a_harom_elem = []
toroltek = 0

if jatekok > 3:
    i = 0
    szakasz.extend([gyoztesek[i],gyoztesek[i+1],gyoztesek[i+2]])
    while True:
        for d in szakasz:
            if not(d in harom_kulonbozo):
                harom_kulonbozo.append(d)
        if len(szakasz) == len(gyoztesek):
            break
        if len(harom_kulonbozo) < 3:
            i += 1
            szakasz.append(gyoztesek[i+2])
        else:
            break
        harom_kulonbozo.clear()
    while True:
        if len(szakasz) > legtobb_elem:
            a_harom_elem.clear()
            legtobb_elem = len(szakasz)
            for c in szakasz:
                if not(c in a_harom_elem):
                    a_harom_elem.append(c)
        if len(szakasz) + toroltek == len(gyoztesek):
            break
        egyenlo = False
        kovetkezo = gyoztesek[len(szakasz) + toroltek]
        for a in szakasz:
            if kovetkezo == a:
                egyenlo = True
                break
        if egyenlo == False:
            while True:
                for b in szakasz:
                    if not (b in ketto_kulonbozo):
                        ketto_kulonbozo.append(b)
                if len(ketto_kulonbozo) > 2:
                    szakasz.remove(szakasz[0])
                    toroltek += 1
                else:
                    break
                ketto_kulonbozo.clear()
        szakasz.append(kovetkezo)
else:
    legtobb_elem = len(gyoztesek)
    for e in gyoztesek:
        if not(e in a_harom_elem):
            a_harom_elem.append(e)

print(legtobb_elem)
for d in a_harom_elem:
    print(d,end=" ")