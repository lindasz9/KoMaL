N, M, DB, T = map(int, input().split())
indulasi_helyek = input().split(" / ")
for i in range(DB):
    indulasi_helyek[i] = indulasi_helyek[i].split()
    indulasi_helyek[i][0] = int(indulasi_helyek[i][0])
    indulasi_helyek[i][1] = int(indulasi_helyek[i][1])

for i in range(T):
    for j in indulasi_helyek:
        if j[2] == "L":
            if j[0] != N:
                j[0] += 1
            else:
                j[0] -= 1
                j[2] == "F"
        elif j[2] == "F":
            if j[0] != 1:
                j[0] -= 1
            else:
                j[0] += 1
                j[2] == "L"
        elif j[2] == "J":
            if j[1] != M:
                j[1] += 1
            else:
                j[1] -= 1
                j[2] == "B"
        else:
            if j[1] != 1:
                j[1] -= 1
            else:
                j[1] += 1
                j[2] == "J"
    ellenorzes = []
    for j in indulasi_helyek:
        if len(ellenorzes) != 0:
            for k in ellenorzes:
                if j[0] == k[0]:
                    if j[1] == k[1]:
                        print(i + 1)
                        exit()
        ellenorzes.append(j)