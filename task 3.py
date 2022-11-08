import random
file = open('polynomial', 'w')

def f(x):
    w = ''
    for i in range(x, -1, -1):
        rand = random.randint(0, 100)
        if rand != 0:
            if (i != 0) and (i != 1) and (i != x):
                w += ' + ' + str(rand)
                w += '*x^' + str(i)
            elif i == x:
                w += str(rand)
                w += '*x^' + str(i)
            elif i == 1:
                w += ' + '
                w += str(rand) + '*x'
            elif i == 0:
                w += ' + ' + str(rand)
    return w


file.write(f(9))