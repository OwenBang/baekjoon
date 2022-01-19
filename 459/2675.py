def qr(*argc):
    for i in argc[1]:
        for j in range(int(argc[0])):
            print(i, end='')
    print()

T = int(input())
for t in range(T):
    qr(*input().split())