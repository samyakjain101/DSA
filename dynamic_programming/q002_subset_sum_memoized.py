def subset_sum(arr, sum, n):
    if sum == 0:
        return True
    if n == 0:
        return False

    if dp[n][sum] != -1:
        return dp[n][sum]

    if sum >= arr[n-1]:
        dp[n][sum] = (
            subset_sum(arr, sum-arr[n-1], n-1) or
            subset_sum(arr, sum, n-1))
        return dp[n][sum]
    else:
        dp[n][sum] = subset_sum(arr, sum, n-1)
        return dp[n][sum]


if __name__ == "__main__":
    arr = [2, 3, 5, 8]
    sum = 11
    n = len(arr)
    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(subset_sum(arr, sum, n))
