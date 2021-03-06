def mcm(matrix, i, j):
    if i >= j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mini = float('inf')
    for k in range(i, j):

        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = mcm(matrix, i, k)
            dp[i][k] = left

        if dp[k+1][j] != -1:
            right = dp[k+1][j]
        else:
            right = mcm(matrix, k+1, j)
            dp[k+1][j] = right

        temp_ans = (left +
                    right +
                    matrix[i-1]*matrix[k]*matrix[j])
        mini = min(temp_ans, mini)

    dp[i][j] = mini
    return dp[i][j]


if __name__ == "__main__":
    matrix = [10, 20, 30, 40, 30]
    i = 1
    j = len(matrix) - 1

    dp = [[-1]*(j+1) for _ in range(j+1)]
    print(mcm(matrix, i, j))
