a = [2, 3, 5, 9, 3, 1]
d = []
for i in range(0, len(a)):
    if i % 2 != 0:
        d.append(a[i])
print(sum(d))