def solve(arr, n, sum):
    dp = [[-1]*(sum+1) for _ in range(n+1)]

    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, sum+1):
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    arr = [1, 1, 2, 3]
    difference = 1
    n = len(arr)
    total = sum(arr)

    # Calculation
    # subset1_sum + subset2_sum = total
    # subset1_sum - subset2_sum = difference
    # 2*subset1_sum = total + difference
    # subset1_sum = (total + difference) / 2

    subset1_sum = (total + difference) // 2

    # Now count number of subsets in arr with sum = subset1_sum
    print(solve(arr, n, subset1_sum))
