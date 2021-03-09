def solve(coin, n, sum):
    if sum == 0:
        return 0
    if n == 0:
        return float('inf')

    if dp[n][sum] != -1:
        return dp[n][sum]

    if sum >= coin[n-1]:
        dp[n][sum] = min(
            1 + solve(coin, n, sum-coin[n-1]),
            solve(coin, n-1, sum))
        return dp[n][sum]
    else:
        dp[n][sum] = solve(coin, n-1, sum)
        return dp[n][sum]


if __name__ == "__main__":
    coin = [25, 10, 5]
    n = len(coin)
    sum = 30
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(solve(coin, n, sum))
