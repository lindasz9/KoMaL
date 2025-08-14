eletkorok_szama = int(input())
eletkorok = input().split()
eletkorok_eredeti = []
eletkorok_eredeti2 = []
eletkorok_eredeti3 = []
for m in eletkorok:
    eletkorok_eredeti.append(int(m))
    eletkorok_eredeti2.append(int(m))
    eletkorok_eredeti3.append(int(m))
eletkorok_2 = []

csoport = []
int_csoport = []
rendezett_csoport = []
legnagyobb_csoport = []
csoport_letszama = []
csoportok_szama = 0
legnagyobb_letszam = 0
elso = 0
utolso = 0

hossz = eletkorok_szama

for i in range(hossz):
    if len(eletkorok) == 0:
        break
    i = eletkorok[0]
    csoport.append(i)
    eletkorok.remove(i)
    for j in csoport:
        if len(eletkorok) == 0:
            break
        for l in eletkorok:
            eletkorok_2.append(l)
        for k in eletkorok_2:
            if len(eletkorok_2) == 0:
                break
            if int(k) == int(j)-1 or int(k) == int(j)+1 or int(k) == int(j):
                csoport.append(k)
                eletkorok.remove(k)
        eletkorok_2.clear()
    csoport_letszama.append(len(csoport))
    if len(csoport) > legnagyobb_letszam:
        legnagyobb_letszam = len(csoport)
        for n in csoport:
            int_csoport.append(int(n))
        for o in eletkorok_eredeti2:
            for p in int_csoport:
                if o == p:
                    rendezett_csoport.append(o)
                    eletkorok_eredeti2.remove(o)
                    break
        eletkorok_eredeti2.clear()
        for s in eletkorok_eredeti3:
            eletkorok_eredeti2.append(s)
        elso = rendezett_csoport[0]
        utolso = rendezett_csoport[-1]
        elso_index = eletkorok_eredeti.index(elso) + 1
        eletkorok_eredeti.reverse()
        utolso_index = eletkorok_eredeti.index(utolso)
        utolso_index = len(eletkorok_eredeti) - utolso_index
        elso,utolso = 0,0
        int_csoport.clear()
        rendezett_csoport.clear()
        eletkorok_eredeti.reverse()
    csoport.clear()
    csoportok_szama += 1

print(csoportok_szama)
print(legnagyobb_letszam)
print(elso_index,utolso_index)