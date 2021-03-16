from q016_longest_common_subsequence_bottom_up import lcs


if __name__ == "__main__":
    string1, string2 = "geek", "eke"
    n, m = len(string1), len(string2)
    longest_common_subsequence_len = lcs(string1, string2, n, m)
    result = m + n - longest_common_subsequence_len
    print(result)
