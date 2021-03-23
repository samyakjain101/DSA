def solve(eggs, floors):
    if floors <= 1 or eggs == 1:
        return floors

    if dp[eggs][floors] != -1:
        return dp[eggs][floors]

    worst_case_minimum = float('inf')
    for k in range(1, floors+1):
        if dp[eggs-1][k-1] != -1:
            low = dp[eggs-1][k-1]
        else:
            low = solve(eggs-1, k-1)
            dp[eggs-1][k-1] = low

        if dp[eggs][floors-k] != -1:
            high = dp[eggs][floors-k]
        else:
            high = solve(eggs, floors-k)
            dp[eggs][floors-k] = high

        worst_case = 1 + max(
            low,
            high)

        worst_case_minimum = min(
            worst_case,
            worst_case_minimum)

    dp[eggs][floors] = worst_case_minimum
    return worst_case_minimum


if __name__ == "__main__":
    eggs = 2
    floors = 4
    dp = [[-1]*(floors+1) for _ in range(eggs+1)]
    print(solve(eggs, floors))
