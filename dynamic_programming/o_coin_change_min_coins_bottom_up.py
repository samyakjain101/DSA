def solve(coin, n, sum):
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(1, n+1):
        dp[i][0] = 0
    for i in range(1, sum+1):
        dp[0][i] = float('inf')
        dp[1][i] = i // coin[0] if i % coin[0] == 0 else float('inf')

    for i in range(2, n+1):
        for j in range(1, sum+1):
            if j >= coin[i-1]:
                dp[i][j] = min(
                    1 + dp[i][j-coin[i-1]],
                    dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    coin = [25, 10, 5]
    n = len(coin)
    sum = 30
    print(solve(coin, n, sum))
