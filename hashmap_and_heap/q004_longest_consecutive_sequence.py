def longest_consecutive_sequence(arr: list):
    hashmap = dict()
    for num in arr:
        hashmap[num] = True

    for key in hashmap.keys():
        if key - 1 in hashmap:
            hashmap[key] = False

    max_streak_start_point = 0
    max_streak = 0
    for key, value in hashmap.items():
        if value:
            temp_streak_start_point = key
            temp_streak = 1

            while temp_streak_start_point + temp_streak in hashmap:
                temp_streak += 1

            if temp_streak > max_streak:
                max_streak = temp_streak
                max_streak_start_point = temp_streak_start_point

    return [
        i for i in range(max_streak_start_point, max_streak_start_point + max_streak)
    ]


if __name__ == "__main__":
    array = [
        12,
        5,
        1,
        2,
        10,
        2,
        13,
        7,
        11,
        8,
        9,
        11,
        8,
        9,
        5,
        6,
        11,
    ]
    print(longest_consecutive_sequence(array))
