N = int(input())
score = []
for i in range(N):
    A, B, C = map(int, input().split())

    if A == B == C:
        score.append(10000 + 1000 * A)
    elif A == B:
        score.append(1000 + 100 * A)
    elif B == C:
        score.append(1000 + 100 * B)
    elif C == A:
        score.append(1000 + 100 * C)
    else:
        temp = A if A > B else B
        temp = temp if temp > C else C
        score.append(temp * 100)

score.sort(reverse=True)
print(score[0])