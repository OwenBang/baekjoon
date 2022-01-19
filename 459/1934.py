T = int(input())
def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A
def lcm(A, B):
    return A * B / gcd(A, B)
result = []
for i in range(T):
    A, B = map(int, input().split())
    result.append(int(lcm(A, B)))

for i in result:
    print(i)