from q016_longest_common_subsequence_bottom_up import lcs


if __name__ == "__main__":
    string1 = "AXY"
    string2 = "ADXCPY"
    n, m = len(string1), len(string2)

    print(lcs(string1, string2, n, m) == min(n, m))
