N = 0
while not 0 < N < 6:
    N = int(input())
n = pow(10,N)
pont = 0
pontok = []

for i in range(1,n):
    for j in range(1,i+1):
        if i // j * j == i:
            pont += j
    pontok.append(pont)
    pont = 0

max = max(pontok)
max_index = pontok.index(max)

print(max_index+1,end=" ")
print(max)
