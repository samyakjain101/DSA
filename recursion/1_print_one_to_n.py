def print_one_to_n(n):
    if n == 0:
        return
    print_one_to_n(n-1)
    print(n)


if __name__ == "__main__":
    print_one_to_n(7)
