def lrs(string):
    n = len(string)
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if string[i-1] == string[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1])

    return dp[n][n]


if __name__ == "__main__":
    string = "aabb"
    print(lrs(string))
