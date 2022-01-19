A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + 1000 * A)
elif A == B:
    print(1000 + 100 * A)
elif B == C:
    print(1000 + 100 * B)
elif C == A:
    print(1000 + 100 * C)
else:
    temp = A if A > B else B
    temp = temp if temp > C else C
    print(temp * 100)