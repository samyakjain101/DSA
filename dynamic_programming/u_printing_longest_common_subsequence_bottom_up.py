def lcs(string1, string2, n1, n2):
    dp = [[""]*(n2+1) for _ in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + string1[i-1]
            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1])

    return dp[n1][n2]


if __name__ == "__main__":
    string1 = "abcdgh"
    string2 = "abedfhr"
    n1 = len(string1)
    n2 = len(string2)
    print(lcs(string1, string2, n1, n2))
