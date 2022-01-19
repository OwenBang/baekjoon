K, N, M = map(int, input().split())
if (M - K * N) >= 0:
    print(0)
else:
    print(K * N - M)