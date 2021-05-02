def num_of_island(matrix: list):
    n = len(matrix)
    m = len(matrix[0])

    visited = [[False] * m for _ in range(n)]
    islands = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and not visited[i][j]:
                draw_component(matrix, i, j, visited, n, m)
                islands += 1

    return islands


def draw_component(matrix, i, j, visited, n, m):
    if i >= n or j >= m or i < 0 or j < 0:
        return
    if visited[i][j] or matrix[i][j] == 1:
        return

    visited[i][j] = True

    # north
    draw_component(matrix, i - 1, j, visited, n, m)

    # south
    draw_component(matrix, i + 1, j, visited, n, m)

    # east
    draw_component(matrix, i, j - 1, visited, n, m)

    # west
    draw_component(matrix, i, j + 1, visited, n, m)


if __name__ == "__main__":
    arr = [
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    print(num_of_island(arr))
