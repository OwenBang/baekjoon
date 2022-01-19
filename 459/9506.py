a = []
while True:
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            a.append(i)
    temp = 0
    for i in a:
        temp += i
    if temp == n:
        print(n, "=", end=" ")
        for i in a:
            print(i, end=" ")
            if i == a[-1]:
                break
            print("+", end=" ")
        print()
    else:
        print(n, "is NOT perfect.")
    a.clear()
