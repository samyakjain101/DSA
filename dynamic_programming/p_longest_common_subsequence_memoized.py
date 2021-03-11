def lcs(string1, string2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0

    if dp[n1][n2] != -1:
        return dp[n1][n2]

    if string1[n1-1] == string2[n2-1]:
        dp[n1][n2] = 1 + lcs(string1, string2, n1-1, n2-1)
        return dp[n1][n2]
    else:
        dp[n1][n2] = max(
            lcs(string1, string2, n1-1, n2),
            lcs(string1, string2, n1, n2-1))
        return dp[n1][n2]


if __name__ == "__main__":
    string1 = "abcdgh"
    string2 = "abedfhr"
    n1 = len(string1)
    n2 = len(string2)
    dp = [[-1]*(n2+1) for _ in range(n1+1)]
    print(lcs(string1, string2, n1, n2))
