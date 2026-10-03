from random import randint


def factor(n: int) -> tuple[int, int]:
    d: int = n
    s: int = 0
    while d % 2 == 0:
        d //= 2
        s = s + 1
    return s, d


def isprime(CheckedNumber: int) -> bool:
    if CheckedNumber % 2 == 0:
        return False

    s, d = factor(CheckedNumber - 1)

    for _ in range(64):
        a = randint(2, CheckedNumber - 2)
        x = pow(a, d, CheckedNumber)
        for __ in range(s):
            y = x**2 % CheckedNumber
            if y == 1 and x != 1 and x != CheckedNumber - 1:
                return False

            x = y
        try:
            if y != 1:
                return False
        except:
            pass
    return True


def twoRandomPrimes() -> tuple(int, int):

    num1 = 0
    num2 = 0

    prime = False

    while not prime:
        num1 = randint((2**1023), (2**1024))
        prime = isprime(num1)

    prime = False
    while not prime:
        num2 = randint((2**1023), (2**1024))
        prime = isprime(num2)

    return num1, num2


# x = eval(input("num:"))


print(twoRandomPrimes())
