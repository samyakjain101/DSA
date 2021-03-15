def lcs(string1, string2, n, m):

    for i in range(1, n+1):
        for j in range(1, m+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1])


if __name__ == "__main__":
    string1 = "AGGTAB"
    string2 = "GXTXAYB"
    n, m = len(string1), len(string2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    lcs(string1, string2, n, m)

    i, j = n, m
    result = ''
    while i > 0 and j > 0:
        if string1[i-1] == string2[j-1]:
            result += string1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                result += string2[j-1]
                j -= 1
            else:
                result += string1[i-1]
                i -= 1

    while i > 0:
        result += string1[i-1]
        i -= 1

    while j > 0:
        result += string2[j-1]
        j -= 1

    print(result[::-1])
