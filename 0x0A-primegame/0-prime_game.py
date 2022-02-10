#!/usr/bin/python3
"""Prime Game
"""


def sieveOfEratosthenes(n):
    """return prime numbers upto n"""
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p] is True]


def isWinner(x, nums):
    """return name of the player that won the most round"""
    countMaria = 0
    countBen = 0
    for n in range(x):
        primes = sieveOfEratosthenes(nums[n])
        if len(primes) % 2 != 0:
            countMaria += 1
        else:
            countBen += 1
    if countMaria > countBen:
        return "Maria"
    elif countBen > countMaria:
        return "Ben"
    else:
        return None
