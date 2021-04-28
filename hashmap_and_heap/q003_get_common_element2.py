def get_common_element(string1: str, string2: str):
    hash1 = dict()

    for char in string1:
        if char in hash1:
            hash1[char] += 1
        else:
            hash1[char] = 1

    common = []
    for char in string2:
        if char in hash1:
            common.append(char)

            if hash1[char] == 1:
                hash1.pop(char)
            else:
                hash1[char] -= 1

    return common


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(get_common_element(str1, str2))
