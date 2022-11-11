d = input('введите текс содержащий слова с абв: ')+' '


def f(x):
    e = []
    t = ''
    for i in range(0, len(x)):
        if x[i] != ' ':
            t += x[i]
        else:
            e.append(t)
            t = ''
    for j in range(0, len(e)):
        r = e[j]
        if 'абв' in r:
            e[j] = ''
    q = ''
    for y in range(0, len(e)):
        if e[y] != '':
            q += e[y]+' '
    print(q)

f(d)