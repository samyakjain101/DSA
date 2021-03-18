from collections import defaultdict


def def_value():
    return None


def solve(string, i, j, bool_required):
    if i > j:
        return 0
    if i == j:
        return (1 if bool_required ==
                (True if string[i] == 'T' else False)
                else 0)

    key = f'{i} {j} {bool_required}'
    if dp[key] is not None:
        return dp[key]

    ans = 0
    for k in range(i, j):
        if string[k] not in {'|', '&', '^'}:
            continue

        leftFalse = solve(string, i, k-1, False)
        leftTrue = solve(string, i, k-1, True)
        rightFalse = solve(string, k+1, j, False)
        rightTrue = solve(string, k+1, j, True)

        if string[k] == '|':
            if bool_required:
                ans += (leftTrue * rightFalse
                        + leftTrue * rightTrue
                        + leftFalse * rightTrue)
            else:
                ans += leftFalse * rightFalse
        elif string[k] == '&':
            if bool_required:
                ans += leftTrue * rightTrue
            else:
                ans += (leftTrue * rightFalse
                        + leftFalse * rightTrue
                        + leftFalse * rightFalse)
        elif string[k] == '^':
            if bool_required:
                ans += leftTrue * rightFalse + leftFalse * rightTrue
            else:
                ans += leftFalse * rightFalse + leftTrue * rightTrue

    dp[key] = ans
    return ans


if __name__ == "__main__":
    string = "T|T&F^T"
    i = 0
    j = len(string) - 1
    dp = defaultdict(def_value)
    print(solve(string, i, j, True))
