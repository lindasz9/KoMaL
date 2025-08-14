N, DB = map(int, input().split())

szamok = []
for a in range(N):
    szamok.append(a+1)

E_szamok, V_szamok, C_szamok = [], [], []
for b in range(DB):
    E, V, C = map(int, input().split())
    E_szamok.append(E)
    V_szamok.append(V)
    C_szamok.append(C)

for e in range(DB):
    E = E_szamok[e]
    V = V_szamok[e]
    C = C_szamok[e]
    if C > V:
        C = C - V + E - 2
    else:
        C -= 1
    kivagas = szamok[E-1:V]
    for c in kivagas:
        szamok.remove(c)
    hely = 1
    for d in kivagas:
        szamok.insert(C+hely, d)
        hely += 1

for f in range(DB):
    f += 1
    print(szamok.index(f)+1,end=" ")
print()
for g in range(DB):
    print(szamok[g],end=" ")