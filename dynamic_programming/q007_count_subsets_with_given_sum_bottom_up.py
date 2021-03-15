def count_subsets_with_sum(arr, n, sum):
    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = 1
    for i in range(1, sum+1):
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j >= arr[i-1]:
                dp[i][j] = (
                    dp[i-1][j-arr[i-1]] + dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    n = len(arr)
    sum = 10

    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(count_subsets_with_sum(arr, n, sum))
