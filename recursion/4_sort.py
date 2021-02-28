def insert(sorted_arr, last):
    if not sorted_arr or sorted_arr[-1] <= last:
        sorted_arr.append(last)
        return
    end = sorted_arr.pop()
    insert(sorted_arr, last)
    sorted_arr.append(end)


def sort(arr):
    if len(arr) == 0:
        return
    last = arr.pop()
    sort(arr)
    insert(arr, last)


if __name__ == "__main__":
    arr = [52, 0, -63, 4, 0, 99, 4, -514651651, 651465165162, 556, -5654]
    sort(arr)
    print(arr)
