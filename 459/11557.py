T = int(input())

for i in range(T):
    N = int(input())
    dic = {}
    for j in range(N):
        S, L = input().split()
        dic[str(S)] = int(L)
    max_key = max(dic, key = dic.get)
    print(max_key)
