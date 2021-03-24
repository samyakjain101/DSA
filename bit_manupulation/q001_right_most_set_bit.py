"""Problem statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/print-value-of-rsb-mask-official/ojquestion
"""


def rsb(n):
    twos_complement = -n
    return bin(n & twos_complement)[2:]


if __name__ == "__main__":
    n = 58
    print(rsb(n))
