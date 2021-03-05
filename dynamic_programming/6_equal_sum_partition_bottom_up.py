def equal_sum_partition(arr, n, sum):
    dp[0][0] = True
    for i in range(1, n+1):
        dp[i][0] = True
    for i in range(1, sum+1):
        dp[0][i] = False

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if sum >= arr[i-1]:
                dp[i][j] = (
                    dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    n = len(arr)
    sum = sum(arr)

    if sum % 2 != 0:
        print(False)
    else:
        sum = int(sum/2)
        dp = [[-1]*(sum+1) for _ in range(n+1)]
        print(equal_sum_partition(arr, n, sum))
