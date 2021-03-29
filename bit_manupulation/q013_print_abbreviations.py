"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/abrreviation1-using-bits-official/ojquestion#

"""


def solve(string, n):
    for i in range(1 << n):
        temp = ""
        count = 0
        for idx, char in enumerate(string):
            if i & (1 << (n - 1 - idx)) == 0:
                if count > 0:
                    temp += str(count)
                    count = 0
                temp += string[idx]
            else:
                count += 1

        if count > 0:
            temp += str(count)

        print(temp)


if __name__ == "__main__":
    word = input()
    solve(word, len(word))
