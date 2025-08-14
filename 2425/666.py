n, h = map(int, input().split())
tavolsagok = sorted(list(map(int, input().split())))

elozo, repulok = 0, 0
for i in tavolsagok:
    if i - h > elozo:
        repulok += 1
    elozo = i

print(repulok)