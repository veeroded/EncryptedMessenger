from PrimeNumbers import twoRandomPrimes
from StringHelper import stringTointeger, integerToString
from math import lcm


def keyGen():

    p, q = twoRandomPrimes()

    while p == q:
        p, q = twoRandomPrimes()

    public = [p * q]

    lmbmodnum = lcm(p - 1, q - 1)

    e = 65_537
    public.append(e)
    private = pow(e, -1, lmbmodnum)

    return public, private


def OAEP(Message: int) -> int:
    pass


def encrypt(Message: int, pubKey: list[int]) -> int:
    n, e = pubKey
    assert Message < n, "message too large for modulus"
    return pow(Message, e, n)


def decrypt(CiperText: int, privKey: int, pubkey: list[int]) -> int:
    return pow(CiperText, privKey, pubkey[0])


def ReverseOAEP(
    Message: int,
):
    pass
