class Pair:
    def __init__(self, vertex: int, psf: str):
        self.vertex = vertex
        self.psf = psf


class Edge:
    def __init__(self, src: int, nbr: int, weight: int):
        self.src = src
        self.nbr = nbr
        self.weight = weight


class Graph:
    def __init__(self, graph_arr: list, vertices: int):
        self.graph = [[] for _ in range(vertices)]

        for edge in graph_arr:
            v1, v2, wt = edge
            e1 = Edge(src=v1, nbr=v2, weight=wt)
            e2 = Edge(src=v2, nbr=v1, weight=wt)

            self.graph[v1].append(e1)
            self.graph[v2].append(e2)

    def dfs_iterative(self, source: int):
        visited = [False] * len(self.graph)
        stack = [Pair(vertex=source, psf=f"{source}")]

        while stack:
            top = stack.pop()

            if visited[top.vertex]:
                continue

            visited[top.vertex] = True
            print(f"{top.vertex}@{top.psf}")

            for edge in self.graph[top.vertex]:
                if not visited[edge.nbr]:
                    stack.append(Pair(vertex=edge.nbr, psf=f"{top.psf}{edge.nbr}"))


if __name__ == "__main__":
    vertices = 7
    k = 8
    arr = [
        [0, 1, 10],
        [1, 2, 10],
        [2, 3, 10],
        [0, 3, 10],
        [3, 4, 10],
        [4, 5, 10],
        [5, 6, 10],
        [4, 6, 10],
    ]
    g = Graph(arr, vertices)
    source = 2
    g.dfs_iterative(source)
