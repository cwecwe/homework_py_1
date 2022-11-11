d = input('введите строку содержащую абв: ')


def f(x):
    while 'абв' in x:
        x = x.replace('абв', '', 1)
    print(x)

f(d)