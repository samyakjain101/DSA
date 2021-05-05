import pathmagic  # noqa
from data_structure.min_heap import MinHeap as PriorityQueue


class Pair:
    def __init__(self, vertex: int, acquired_vertex: int, weight: int):
        self.vertex = vertex
        self.acquired_vertex = acquired_vertex
        self.weight = weight

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        return False

    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        return False

    def __eq__(self, other):
        if self.weight == other.weight:
            return True
        return False


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

    def prims(self):
        visited = [False] * len(self.graph)

        q = PriorityQueue(len(self.graph))
        q.insert(Pair(vertex=0, acquired_vertex=-1, weight=0))

        while q.size:
            removed = q.remove_min()

            if visited[removed.vertex]:
                continue

            visited[removed.vertex] = True

            if removed.acquired_vertex != -1:
                print(f"[{removed.vertex}-{removed.acquired_vertex}@{removed.weight}]")

            for edge in self.graph[removed.vertex]:
                if not visited[edge.nbr]:
                    q.insert(
                        Pair(
                            vertex=edge.nbr,
                            acquired_vertex=removed.vertex,
                            weight=edge.weight,
                        )
                    )


if __name__ == "__main__":
    vertices = 7
    k = 8
    arr = [
        [0, 1, 10],
        [1, 2, 10],
        [2, 3, 10],
        [0, 3, 40],
        [3, 4, 2],
        [4, 5, 3],
        [5, 6, 3],
        [4, 6, 8],
    ]
    g = Graph(arr, vertices)
    g.prims()
