import random
import textwrap

B, M, S = map(int,input().split())
szavak = []
gyakok = []
szavak_gyakok = {}

def generalas_szo():
    return random.choices(szavak,weights=gyakok,k=1)[0]

def generalas_mondat():
    szavak_szama = random.randint(1,S)
    mondat = []
    for i in range(szavak_szama):
        random_szo = generalas_szo()
        if i == 0:
            random_szo = random_szo.capitalize()
        mondat.append(random_szo)
    if szavak_szama > 10:
        mondat.insert(random.randint(1,S-1),",")
    mondat.append(".")
    kor = len(mondat)
    kesz_mondat = ""
    for j in range(kor):
        if j != kor-1:
            if mondat[j+1] == "," or mondat[j+1] == ".":
                ending = ""
            else:
                ending = " "
        kesz_mondat += mondat[j] + ending
    return kesz_mondat

def generalas_bekezdes():
    kesz_bekezdes = ""
    for i in range(M):
        random_mondat = generalas_mondat()
        kesz_bekezdes += random_mondat + " "
    return kesz_bekezdes.strip()

def generalas_szoveg():
    try:
        szelesseg = 40
    except:
        szelesseg = 40
    for i in range(B):
        if i > 0:
            print("   ",end="")
        random_bekezdes = generalas_bekezdes()
        print(textwrap.fill(random_bekezdes,width=szelesseg))

with open("eng5000","r") as file:
    for line in file:
        szo, gyak = line.strip().split()
        szavak.append(szo)
        gyakok.append(int(gyak))
    szavak_gyakok = dict(zip(szavak,gyakok))

generalas_szoveg()
