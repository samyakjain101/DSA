from q016_longest_common_subsequence_bottom_up import lcs


if __name__ == "__main__":
    string1 = "agbcba"
    n = len(string1)

    string2 = string1[::-1]
    m = len(string2)

    longest_common_subsequence_len = lcs(string1, string2, n, m)
    print(longest_common_subsequence_len)
