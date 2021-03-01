import math


def power_sum(X, N, larger_than):
    """
    https://www.hackerrank.com/challenges/the-power-sum/problem
    """
    if X == 0:
        return 1
    return sum(
        power_sum(X - i ** N, N, i) for i in range(
            larger_than + 1, math.ceil(math.pow(X + 1, 1 / N))))


if __name__ == "__main__":
    X = 100
    N = 2
    print(power_sum(X, N, 0))
