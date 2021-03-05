def equal_sum_partition(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False

    if dp[n][sum] != -1:
        return dp[n][sum]

    if sum >= arr[n-1]:
        dp[n][sum] = (
            equal_sum_partition(arr, n-1, sum-arr[n-1]) or
            equal_sum_partition(arr, n-1, sum)
        )
        return dp[n][sum]
    else:
        dp[n][sum] = equal_sum_partition(arr, n-1, sum)
        return dp[n][sum]


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    n = len(arr)
    sum = sum(arr)

    dp = [[-1]*(sum+1) for _ in range(n+1)]
    if sum % 2 != 0:
        print(False)
    else:
        print(equal_sum_partition(arr, n, int(sum/2)))
