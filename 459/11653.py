def calc(N):
    d = 2
    A = [];
    while d <= N:
        if N % d == 0:
            N = N // d
            A.append(d)
            d -= 1
        d += 1
    for i in range(len(A)):
        print(A[i])

calc(int(input()))
