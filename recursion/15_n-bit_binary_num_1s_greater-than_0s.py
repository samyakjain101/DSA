def n_bit_binary(n, ones, zeroes, output):
    """
    Print N-bit binary numbers having more 1’s than 0’s for any prefix
    """
    if n == 0:
        print(output)
        return
    n_bit_binary(n-1, ones+1, zeroes, output + '1')
    if ones > zeroes:
        n_bit_binary(n-1, ones, zeroes+1, output + '0')


if __name__ == "__main__":
    n = 4
    ones = zeroes = 0
    output = ''
    n_bit_binary(n, ones, zeroes, output)
