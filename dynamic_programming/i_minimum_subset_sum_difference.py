def solve(arr, n, upper):
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = True
    for i in range(1, upper+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, upper+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][upper]


if __name__ == "__main__":
    arr = [1, 5, 11, 6]
    n = len(arr)
    upper = sum(arr)
    dp = [[-1]*(upper+1) for _ in range(n+1)]
    solve(arr, n, upper)

    subset1_upper = upper // 2
    mini = float('inf')
    for i in range(subset1_upper+1):
        if not dp[n][i]:
            continue
        difference = upper - 2*i
        if difference < mini:
            mini = difference

    print(mini)
