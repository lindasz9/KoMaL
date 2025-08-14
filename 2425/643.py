szam = int(input(""))
negyzetosszeg = 0

for i in range(1,szam+1):
    if szam % i == 0:
        negyzetosszeg += i*i

if negyzetosszeg % szam == 0:
    print("IGEN")
else:
    print("NEM")