def prime_number(n):
    """Returns all prime number from (1 ,n]

    Time complexity- O(N * loglogN)
    """

    # Initialize sieve as True
    sieve = [True] * (n + 1)

    # 0 and 1 are not prime
    sieve[0] = sieve[1] = False

    prime_nos = []
    for num, is_prime in enumerate(sieve):
        if is_prime:
            prime_nos.append(num)

            # Mark multiples of num as not prime
            # Start marking from (num * num) to n
            # All num less than num * num are already covered
            # by previous prime nos.

            for i in range(num*num, n+1, num):
                sieve[i] = False

    return prime_nos


if __name__ == "__main__":
    prime_nos = prime_number(100)
    print(prime_nos)
