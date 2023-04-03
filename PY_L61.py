from random import randint

SIZE = 100
_secret = 'qwerty'  # защищенная переменная
__top_secret = '1q2w3e4r5t6y'


def func(a: int, b: int) -> str:
    z = f'в диапазоне от {a} до {b} полуили {randint (a,b)}'
    return z


result = func(1, 6)
z = randint(1, 50)
print(z)
