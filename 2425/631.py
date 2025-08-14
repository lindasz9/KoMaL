import random

ABC = input()
ABC = ABC.split()

loop = 0
for i in ABC:
    loop += 1
    if loop == 1:
        A = int(i)
    elif loop == 2:
        B = int(i)
    else:
        C = int(i)

a_p = 0
b_p = 0
c_p = 0

kor = 0
while kor < 10000:
    a_sz = random.randint(1, 100)
    b_sz = random.randint(1, 100)
    c_sz = random.randint(1, 100)
    if (a_sz ** 2 + b_sz ** 2 == c_sz ** 2 or
        a_sz ** 2 + c_sz ** 2 == b_sz ** 2 or
        b_sz ** 2 + c_sz ** 2 == a_sz ** 2 or
        a_sz == b_sz and c_sz < (a_sz + b_sz) or
        a_sz == c_sz and b_sz < (a_sz + c_sz) or
        b_sz == c_sz and a_sz < (b_sz + c_sz)):
        a_p += A
    elif (a_sz > b_sz + c_sz or
        b_sz > a_sz + c_sz or
        c_sz > a_sz + b_sz):
        c_p += C
    else:
        b_p += B
    kor += 1

print(f"{a_p} {b_p} {c_p}")

