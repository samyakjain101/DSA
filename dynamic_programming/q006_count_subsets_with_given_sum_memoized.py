def count_subsets_with_sum(arr, n, sum):
    if sum == 0:
        return 1
    if n == 0:
        return 0

    if dp[n][sum] != -1:
        return dp[n][sum]

    if sum >= arr[n-1]:
        dp[n][sum] = (
            count_subsets_with_sum(arr, n-1, sum-arr[n-1]) +
            count_subsets_with_sum(arr, n-1, sum))
        return dp[n][sum]
    else:
        dp[n][sum] = count_subsets_with_sum(arr, n-1, sum)
        return dp[n][sum]


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 8, 10]
    n = len(arr)
    sum = 10

    dp = [[-1]*(sum+1) for _ in range(n+1)]
    print(count_subsets_with_sum(arr, n, sum))
