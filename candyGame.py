import random


def person():
    print('Ваш ход')
    ate_candy = int(input('введите число от 1 до 28: '))
    while (ate_candy > 28) or (ate_candy < 1):
        ate_candy = int(input('введите правильно: '))
    return ate_candy

def bot():
    print('Ходит бот')
    ate_candy = random.randint(1, 28)
    print(ate_candy)
    return ate_candy


sweets = 2021
motion = random.randint(0, 1)
while sweets > 0:
    print('сейчас осталось ', sweets, ' конфет')
    if motion == 0:
        sweets -= person()
        motion = 1
    else:
        sweets -= bot()
        motion = 0
if motion == 0:
    print('бот выиграл')
else:
    print('поздравляем вы выиграли!!!')
