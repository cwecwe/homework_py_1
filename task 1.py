
def f(x):
    t = []
    for i in range(x, 0, -1):
        if x % i == 0:
            t.append(i)
    t = t[::-1]
    return t


N = int(input('введите натуральное число N: '))
print(f(N))