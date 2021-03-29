"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/reduce-n-to-1-official/ojquestion

"""


def solve(num):
    steps = 0

    while num != 1:
        if num % 2 == 0:
            num /= 2
        elif num == 3:
            num -= 1
        elif num % 4 == 3:
            num += 1
        elif num % 4 == 1:
            num -= 1

        steps += 1

    return steps


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
