import random

kockak_eredeti, kiserletek = map(int,input().split())
kockak = kockak_eredeti
atlag = 0

for kiserlet in range(kiserletek):
    kockak = kockak_eredeti
    dobassorozat = 0
    while kockak != 0:
        hatosak = 0
        for dobas in range(kockak):
            if random.randint(1,6) == 6:
                hatosak += 1
        kockak -= hatosak
        dobassorozat += 1
    atlag += dobassorozat

print(round((atlag / kiserletek),1))

