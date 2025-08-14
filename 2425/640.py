lampak_szama = int(input())
lampak_helyei = input().split()
int_lampak_helyei = []
for j in lampak_helyei:
    int_lampak_helyei.append(int(j))

megvilagitottak = []
megvilagitottak_eredeti = []
parosak = []
paratlanok = []
feleslegesek = []
megvilagitottak_felesleges = []
lampa_nelkuliek = []
megvilagitottak_lampa_nelkuli = []
negy_valtozas = []
harom_valtozas = []
ketto_valtozas = []
egy_valtozas = []
nulla_valtozas = []

for k in int_lampak_helyei:
    megvilagitottak.append(k)
    megvilagitottak_eredeti.append(k)

for i in megvilagitottak_eredeti:
    if i > 2 and i-2 not in megvilagitottak:
        megvilagitottak.append(i-2)
    if i < 49 and i+2 not in megvilagitottak:
        megvilagitottak.append(i+2)
    if i % 2 == 0 and i-1 not in megvilagitottak:
        megvilagitottak.append(i-1)
    if i % 2 == 1 and i+1 not in megvilagitottak:
        megvilagitottak.append(i+1)

for l in range(50):
    l += 1
    if l % 2 == 0:
        parosak.append(l)
    if l % 2 == 1:
        paratlanok.append(l)

print("1. feladat")
eleje = ""
for m in paratlanok:
    if m in megvilagitottak:
        eleje = "."
    else:
        eleje = " "
    print(f"{eleje}{m}",end="")
print()
for n in parosak:
    if n in megvilagitottak:
        eleje = "."
    else:
        eleje = " "
    print(f"{eleje}{n}",end="")
print()

print("2. feladat Felesleges lámpaoszlopok: ",end="")
for p in megvilagitottak_eredeti:
    megvilagitottak_eredeti.remove(p)
    for r in int_lampak_helyei:
        megvilagitottak_felesleges.append(r)
    for o in megvilagitottak_eredeti:
        if o > 2 and o-2 not in megvilagitottak_felesleges:
            megvilagitottak_felesleges.append(o-2)
        if o < 49 and o+2 not in megvilagitottak_felesleges:
            megvilagitottak_felesleges.append(o+2)
        if o % 2 == 0 and o-1 not in megvilagitottak_felesleges:
            megvilagitottak_felesleges.append(o-1)
        if o % 2 == 1 and o+1 not in megvilagitottak_felesleges:
            megvilagitottak_felesleges.append(o+1)
    if len(megvilagitottak_felesleges) == len(megvilagitottak):
        feleslegesek.append(p)
    megvilagitottak_eredeti.append(p)
    megvilagitottak_eredeti.sort()
    megvilagitottak_felesleges.clear()
for q in feleslegesek:
    print(q,end=" ")
print()

print("3. feladat")
for t in range(50):
    t += 1
    if t not in megvilagitottak_eredeti:
        lampa_nelkuliek.append(t)
for u in lampa_nelkuliek:
    megvilagitottak_eredeti.append(u)
    for v in int_lampak_helyei:
        megvilagitottak_lampa_nelkuli.append(v)
    megvilagitottak_lampa_nelkuli.append(u)
    for s in megvilagitottak_eredeti:
        if s > 2 and s-2 not in megvilagitottak_lampa_nelkuli:
            megvilagitottak_lampa_nelkuli.append(s-2)
        if s < 49 and s+2 not in megvilagitottak_lampa_nelkuli:
            megvilagitottak_lampa_nelkuli.append(s+2)
        if s % 2 == 0 and s-1 not in megvilagitottak_lampa_nelkuli:
            megvilagitottak_lampa_nelkuli.append(s-1)
        if s % 2 == 1 and s+1 not in megvilagitottak_lampa_nelkuli:
            megvilagitottak_lampa_nelkuli.append(s+1)
    if len(megvilagitottak_lampa_nelkuli) - len(megvilagitottak) == 4:
        negy_valtozas.append(u)
    if len(megvilagitottak_lampa_nelkuli) - len(megvilagitottak) == 3:
        harom_valtozas.append(u)
    if len(megvilagitottak_lampa_nelkuli) - len(megvilagitottak) == 2:
        ketto_valtozas.append(u)
    if len(megvilagitottak_lampa_nelkuli) - len(megvilagitottak) == 1:
        egy_valtozas.append(u)
    if len(megvilagitottak_lampa_nelkuli) - len(megvilagitottak) == 0:
        nulla_valtozas.append(u)
    megvilagitottak_eredeti.remove(u)
    megvilagitottak_lampa_nelkuli.clear()
print("4 változás: ",end="")
for w in negy_valtozas:
    print(w,end=" ")
print()
print("3 változás: ", end="")
for x in harom_valtozas:
    print(x, end=" ")
print()
print("2 változás: ",end="")
for y in ketto_valtozas:
    print(y,end=" ")
print()
print("1 változás: ",end="")
for z in egy_valtozas:
    print(z,end=" ")
print()
print("0 változás: ",end="")
for a in nulla_valtozas:
    print(a,end=" ")
print()

print("4. feladat")
print("Szükséges új oszlopok száma: ",end="")
