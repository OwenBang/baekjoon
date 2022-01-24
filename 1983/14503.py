N, M = map(int, input().split())
r, c, d = map(int, input().split())
dix = [0, 1, 0, -1]
diy = [-1, 0, 1, 0]
cleanmap = []
for i in range(N):
    temp = []
    temp = list(map(int, input().split()))
    cleanmap.append(temp)

cnt = 0
flag = 0
while True:
    if cleanmap[r][c] == 0:
        cleanmap[r][c] = 3
        cnt += 1
    if cleanmap[r + diy[d - 1]][c + dix[d - 1]] == 0:
        d -= 1
        if d == -1:
            d = 3
        r += diy[d]
        c += dix[d]
        flag = 0
        continue
    elif flag == 4:
        r -= diy[d]
        c -= dix[d]
        if cleanmap[r][c] == 1:
            break
        flag = 0
        continue
    elif cleanmap[r + diy[d - 1]][c + dix[d - 1]] == 3 or cleanmap[r + diy[d - 1]][c + dix[d - 1]] == 1:
        d -= 1
        flag += 1
        if d == -1:
            d = 3
        continue
print(cnt)