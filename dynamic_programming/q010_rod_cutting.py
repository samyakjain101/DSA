def solve(price, n):
    size = len(price)
    dp = [[0]*(n+1) for _ in range(size+1)]

    for i in range(1, size+1):
        for j in range(1, n+1):
            if j >= length[i-1]:
                dp[i][j] = max(
                    price[i-1] + dp[i][j-length[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]

    return dp[size][n]


if __name__ == "__main__":
    length = [1, 2, 3, 4, 5, 6, 7, 8]
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    n = len(price)
    print(solve(price, n))
