from collections import defaultdict


def def_value():
    return None


def lcs(string1, string2, n1, n2, count=0):
    if n1 == 0 or n2 == 0:
        return count

    key = f'{n1},{n2},{count}'
    if dp[key]:
        return dp[key]

    if string1[n1-1] == string2[n2-2]:
        dp[key] = lcs(string1, string2, n1-1, n2-1, 1+count)
        return dp[key]
    else:
        dp[key] = max(
            count,
            max(
                lcs(string1, string2, n1-1, n2, 0),
                lcs(string1, string2, n1, n2-1, 0)))
        return dp[key]


if __name__ == "__main__":
    string1 = "abdc1234dgabcdefh"
    string2 = "abed1234abcdeffhr"
    n1 = len(string1)
    n2 = len(string2)
    dp = defaultdict(def_value)
    print(lcs(string1, string2, n1, n2))
