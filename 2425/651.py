db, lepesek = map(int, input().split())
sejtek = input()
szabalyok = {}
for a in range(8):
    szabaly = input().split()
    szabalyok[szabaly[0]] = szabaly[1]

uj_sejtek = sejtek
for c in range(lepesek):
    for b in range(db-1):
           if b == 0:
            continue
        harmas = sejtek[b-1] + sejtek[b] + sejtek[b+1]
        for key,value in szabalyok.items():
            if harmas == key:
                uj_sejtek = uj_sejtek[:b] + value + uj_sejtek[b+1:]
    sejtek = uj_sejtek

print(sejtek.count("S"))

