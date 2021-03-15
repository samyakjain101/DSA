def lcs(string1, string2, n1, n2):
    dp = [[0]*(n2+1) for _ in range(n1+1)]

    maxi = 0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxi = dp[i][j] if dp[i][j] > maxi else maxi
            else:
                dp[i][j] = 0

    return maxi


if __name__ == "__main__":
    string1 = "abdcb"
    string2 = "abedcb"
    n1 = len(string1)
    n2 = len(string2)
    print(lcs(string1, string2, n1, n2))
