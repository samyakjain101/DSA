def subset_sum(arr, sum, n):
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j >= arr[i-1]:
                dp[i][j] = (
                    dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    arr = [2, 3, 5, 8]
    sum = 11
    n = len(arr)
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(subset_sum(arr, sum, n))
