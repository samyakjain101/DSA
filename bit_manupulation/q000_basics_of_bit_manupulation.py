"""Problem statement
https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/basics-of-bit-official/ojquestion
"""


def toggle_bit(n, i):
    toggle_mask = (1 << i)
    return (n ^ toggle_mask)


def unset_bit(n, i):
    off_mask = ~(1 << i)
    return (n & off_mask)


def set_bit(n, i):
    on_mask = (1 << i)
    return (n | on_mask)


def on_or_off(n, i):
    check_mask = (1 << i)
    return False if (n & check_mask) == 0 else True


if __name__ == "__main__":
    n = 57
    i = 3
    j = 3
    k = 3
    m = 3
    print(set_bit(n, i))
    print(unset_bit(n, j))
    print(toggle_bit(n, k))
    print(on_or_off(n, m))
