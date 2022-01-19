def calc(*argc):
    sum = float(argc[0])
    for n in range(1, len(argc)):
        if argc[n] == '@':
            sum = sum * 3
        elif argc[n] == '%':
            sum += 5
        elif argc[n] == '#':
            sum -= 7
    return sum

T = int(input())
for t in range(T):
    ans = calc(*input().split())
    print(f'{ans:.2f}')
