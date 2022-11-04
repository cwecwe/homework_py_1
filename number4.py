e = int(input('введите десятичное число: '))
g = []
while e > 0:
    g.append(e % 2)
    e //= 2
g = g[::-1]
print(g)