#!/usr/bin/python3
"""Make a change module
"""


def makeChange(coins, total):
    """return the smalles combination of possible changes
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    while coins:
        coin = 0
        i = 0
        while total != 0:
            if total < coins[-1] or i == len(coins):
                break
            div = int(total / coins[i])
            mod = total % coins[i]
            if div > 0:
                coin += div
                total = mod
            i += 1
        if total == 0:
            return coin
        coins.pop(0)
    return -1
