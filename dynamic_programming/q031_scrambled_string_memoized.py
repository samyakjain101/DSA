from collections import defaultdict


def def_value():
    return None


def solve(string1, string2):
    n = len(string1)

    if string1 == string2:
        return True
    if n <= 1:
        return False

    key = f'{string1} {string2}'
    if dp[key] is not None:
        print('past')
        return dp[key]

    flag = False
    for i in range(1, n):
        if (
            (solve(string1[:i], string2[n-i:])
                and solve(string1[i:], string2[:n-i]))
            or
            (solve(string1[:i], string2[:i])
                and solve(string1[i:], string2[i:]))
        ):
            flag = True
            break

    dp[key] = flag
    return flag


if __name__ == "__main__":
    string1 = "great"
    string2 = "rgeat"
    if len(string1) != len(string2):
        print(False)
    else:
        dp = defaultdict(def_value)
        print(solve(string1, string2))
