from q016_longest_common_subsequence_bottom_up import lcs


if __name__ == "__main__":
    string = "AXY"
    n = len(string)

    lcs_result = lcs(string, string[::-1], n, n)
    print(n-lcs_result)
