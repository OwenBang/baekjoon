N = int(input())
p = 0
c = 0
for i in range(N):
    temp = int(input())
    if temp == 1:
        p += 1
    elif temp == 0:
        c += 1

if p > c:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")