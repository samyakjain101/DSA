"""Problem statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/kernighans-algo-official/ojquestion
"""


def kernighans(n):

    count = 0
    while n != 0:
        rsb = n & -n
        n -= rsb
        count += 1

    return count


if __name__ == "__main__":
    n = 58
    print(kernighans(n))
