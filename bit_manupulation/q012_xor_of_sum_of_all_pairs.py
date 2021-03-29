"""Problem Statement

https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/bit-manipulation/xor-sum-pair-official/ojquestion#

"""

def solve(array):
    xor = 0
    for num in array:
        xor ^= num*2

    return xor

if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    print(solve(arr))
