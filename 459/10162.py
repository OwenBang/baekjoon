T = int(input())

a = 0
b = 0
c = 0

if T % 10 != 0:
    print(-1)
else:
    while T >= 300:
        T -= 300
        a += 1
    while T >= 60:
        T -= 60
        b += 1
    while T > 0:
        T -= 10
        c += 1
    print(a, b, c)