def knapsack_01(weight, value, W, n):
    for i in range(1, n+1):
        for j in range(1, W+1):
            if j >= weight[i-1]:
                dp[i][j] = max(
                    value[i-1] + dp[i-1][j-weight[i-1]],
                    dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]


if __name__ == "__main__":
    weight = [10, 20, 30]
    value = [60, 100, 120]
    W = 50
    n = len(weight)
    dp = [[0]*(W+1) for _ in range(n+1)]
    print(knapsack_01(weight, value, W, n))
