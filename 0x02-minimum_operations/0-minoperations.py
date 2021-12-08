#!/usr/bin/python3
""" Minimum operation. """
import math


def primeFactorial(n):
    """ resturn list of prime factors of a number. """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    """ add all the prime factors. """
    if n == 0:
        return 0
    return int(sum(primeFactorial(n)))
