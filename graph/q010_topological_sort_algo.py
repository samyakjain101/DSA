class Edge:
    def __init__(self, src: int, nbr: int):
        self.src = src
        self.nbr = nbr


class DirectedGraph:
    def __init__(self, graph_arr: list, vertices: int):
        self.graph = [[] for _ in range(vertices)]

        for edge in graph_arr:
            src, dest = edge
            self.graph[src].append(Edge(src=src, nbr=dest))

    def topological_sort(self):
        visited = [False] * len(self.graph)
        stack = []

        for vertex, is_visited in enumerate(visited):
            if is_visited:
                continue

            self.dfs(vertex, visited, stack)

        return stack[::-1]

    def dfs(self, source: int, visited: list, stack: list):
        if visited[source]:
            return

        visited[source] = True
        for edge in self.graph[source]:
            self.dfs(edge.nbr, visited, stack)

        stack.append(source)


if __name__ == "__main__":
    vertices = 7
    k = 7
    arr = [
        [0, 1],
        [1, 2],
        [2, 3],
        [0, 3],
        [4, 5],
        [5, 6],
        [4, 6],
    ]
    g = DirectedGraph(arr, vertices)
    for i in g.topological_sort():
        print(i)
