X = []
Y = []
for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
if X[0] == X[1]:
    x = X[2]
else:
    x = X[0]
if Y[0] == Y[1]:
    y = Y[2]
else:
    y = Y[0]
print(x, y)