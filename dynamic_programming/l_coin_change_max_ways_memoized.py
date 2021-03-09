def solve(coin, sum, n):
    if sum == 0:
        return 1
    if n == 0:
        return 0

    if dp[n][sum] != -1:
        return dp[n][sum]

    if sum >= coin[n-1]:
        dp[n][sum] = (
            solve(coin, sum-coin[n-1], n) +
            solve(coin, sum, n-1))
        return dp[n][sum]
    else:
        dp[n][sum] = solve(coin, sum, n-1)
        return dp[n][sum]


if __name__ == "__main__":
    coin = [1, 2, 3]
    n = len(coin)
    sum = 5
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(solve(coin, sum, n))
