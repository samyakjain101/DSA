def Kth_symbol(n, k):
    """
    https://leetcode.com/problems/k-th-symbol-in-grammar/
    """

    if n == 1 and k == 1:
        return 0
    if k <= 2**(n-2):
        return Kth_symbol(n-1, k)
    else:
        return int(not Kth_symbol(n-1, k-2**(n-2)))


if __name__ == "__main__":
    n = 5
    k = 11
    print(Kth_symbol(n, k), 'Answer should be 0')
    n = 5
    k = 5
    print(Kth_symbol(n, k), 'Answer should be 1')
