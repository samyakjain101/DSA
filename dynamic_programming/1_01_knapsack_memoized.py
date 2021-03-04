def knapsack_01(weight, value, W, n):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if W >= weight[n-1]:
        dp[n][W] = max(
            value[n-1] + knapsack_01(weight, value, W-weight[n-1], n-1),
            knapsack_01(weight, value, W, n-1))
        return dp[n][W]
    else:
        dp[n][W] = knapsack_01(weight, value, W, n-1)
        return dp[n][W]


if __name__ == "__main__":
    weight = [4, 5, 6]
    value = [1, 2, 3]
    W = 3
    n = len(weight)
    dp = [[-1]*(W+1) for _ in range(n+1)]
    print(knapsack_01(weight, value, W, n))
