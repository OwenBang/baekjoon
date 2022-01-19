T = int(input())
for i in range(T):
    ox = str(input())
    score = 0
    tscore = 0
    for j in ox:
        if j == 'O':
            score += 1
        else:
            score = 0
        tscore += score
    print(tscore)