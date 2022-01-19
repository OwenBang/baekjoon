dish = str(input())
h = 0
for i in range(len(dish)):
    if i == 0:
        h += 10
        continue
    if dish[i] == dish[i - 1]:
        h += 5
    else:
        h += 10
print(h)