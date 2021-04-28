def max_frequency_char(string: str):
    freq = dict()
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    max_freq = 0
    max_freq_key = None
    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            max_freq_key = key

    return max_freq_key


if __name__ == "__main__":
    string_of_char = input()
    print(max_frequency_char(string_of_char))
