a = [2, 3, 4, 5, 6, 7, 1]
c = []
if len(a) % 2 == 0:
    e = int(len(a) / 2)
    for i in range(0, e):
        l = i*-1-1
        c.append(a[i]*a[l])
else:
    g = int(len(a)/2+0.5)
    for i in range(0, g):
        if i != g:
            l = i * -1 - 1
            c.append(a[i]*a[l])
        else:
            c.append(a[i]**2)
print(c)