import random

n = int(input())

szamok = []
for a in range(1,n+1):
    szamok.append(a)
random.shuffle(szamok)
for b in szamok:
    print(b,end=" ")
print()

max = max(szamok)
max_index = szamok.index(max)

def csere(max,max_index):
    for i in range(n-1):
        if i > 0:
            helyes_szamok.append(uj_szamok[-1])
            szamok.remove(uj_szamok[-1])
            max_index = szamok.index(n-i)
        uj_szamok = szamok[max_index::-1] + szamok[max_index+1:]
        if (not max_index == len(szamok) - 1) and (not (max_index == 0)):
            for c in uj_szamok:
                print(c,end=" ")
            for d in helyes_szamok[::-1]:
                print(d,end=" ")
            print()
        uj_szamok = uj_szamok[::-1]
        if not (max_index == len(szamok) - 1):
            for e in uj_szamok:
                print(e,end=" ")
            for f in helyes_szamok[::-1]:
                print(f,end=" ")
            print()
        szamok.clear()
        for g in uj_szamok:
            szamok.append(g)

helyes_szamok = []
csere(max,max_index)