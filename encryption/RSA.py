from .PrimeNumbers import twoRandomPrimes
from math import lcm, floor


def keyGen():

    p, q = twoRandomPrimes()
    public = p * q

    lmbmodnum = lcm(p - 1, q - 1)

    e = 656537
    private = (1 / e) % lmbmodnum

    return public, private


def stringTointeger(Message: str):

    pass
