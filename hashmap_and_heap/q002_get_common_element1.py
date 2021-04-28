def get_common_element(string1: str, string2: str):
    hash1 = set()

    for char in string1:
        hash1.add(char)

    common = []
    for char in string2:
        if char in hash1:
            common.append(char)
            hash1.remove(char)

    return common


if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(get_common_element(str1, str2))
