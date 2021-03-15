def solve(coin, sum, n):
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, sum+1):
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j >= coin[i-1]:
                dp[i][j] = dp[i][j-coin[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    coin = [1, 2, 3]
    n = len(coin)
    sum = 5
    print(solve(coin, sum, n))
