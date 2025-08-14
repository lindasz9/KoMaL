def kulonbozok(resz):
    kulonbozo = []
    for i in resz:
        if i not in kulonbozo and i != 0:
            kulonbozo.append(i)
    return len(kulonbozo)

n, m, k = map(int, input().split())
eloadasok = list(map(int, input().split()))

resz = [eloadasok[i] for i in range(k)]

db = kulonbozok(resz)
keves = [db, 1]
sok = [db, 1]

for i in range(n - k):
    resz.pop(0)
    resz.append(eloadasok[i + k])
    
    db = kulonbozok(resz)
    if db < keves[0]:
        keves = [db, i + 2]
    elif db > sok[0]:
        sok = [db, i + 2]

print(sok[1])
print(keves[1])