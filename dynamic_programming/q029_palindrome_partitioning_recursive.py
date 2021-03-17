def solve(string, i, j):
    if i >= j:
        return 0

    intermediate = string[i:j+1]
    if intermediate == intermediate[::-1]:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mini = float('inf')
    for k in range(i, j):

        if dp[i][k] != -1:
            left = dp[i][k]
        else:
            left = solve(string, i, k)

        if dp[k+1][j] != -1:
            right = dp[k+1][j]
        else:
            right = solve(string, k+1, j)

        temp_ans = left + right + 1
        mini = min(mini, temp_ans)

    dp[i][j] = mini
    return mini


if __name__ == "__main__":
    string = "nitina"
    i = 0
    j = len(string) - 1

    dp = [[-1]*(j+1) for _ in range(j+1)]
    print(solve(string, i, j))
