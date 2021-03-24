"""Problem statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/kernighans-algo-official/ojquestion
"""


def powerof2(n):
    i = 1
    while i * 2 <= n:
        i *= 2

    return i


def josephus(n):
    lsb = powerof2(n)
    remainder = n - lsb
    return 2 * remainder + 1


if __name__ == "__main__":
    n = 4
    print(josephus(n))
