def josephus_problem(circle, killer, k):
    if len(circle) == 1:
        return circle[0]
    killed_idx = ((killer+k-1) % len(circle))
    circle.pop(killed_idx)
    return josephus_problem(circle, killed_idx, k)


if __name__ == "__main__":
    n = 40
    k = 7
    killer = 0
    print(josephus_problem([_ for _ in range(1, n+1)], killer, k))
