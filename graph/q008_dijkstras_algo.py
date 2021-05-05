import pathmagic  # noqa
from data_structure.min_heap import MinHeap as PriorityQueue


class Pair:
    def __init__(self, vertex: int, psf: str, cost: int):
        self.vertex = vertex
        self.psf = psf
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        return False

    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        return False

    def __eq__(self, other):
        if self.cost == other.cost:
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

    def dijkstras_algo(self, vertices: int, source: int):
        visited = [False] * len(self.graph)

        q = PriorityQueue(vertices)
        q.insert(Pair(vertex=source, psf=f"{source}", cost=0))

        while q.size:
            removed = q.remove_min()

            if visited[removed.vertex]:
                continue
            visited[removed.vertex] = True
            print(f"{removed.vertex} via {removed.psf} @ {removed.cost}")

            for edge in self.graph[removed.vertex]:
                if not visited[edge.nbr]:
                    q.insert(
                        Pair(
                            vertex=edge.nbr,
                            psf=f"{removed.psf}{edge.nbr}",
                            cost=removed.cost + edge.weight,
                        )
                    )


if __name__ == "__main__":
    vertices = 7
    k = 9
    arr = [
        [0, 1, 10],
        [1, 2, 10],
        [2, 3, 10],
        [0, 3, 40],
        [3, 4, 2],
        [4, 5, 3],
        [5, 6, 3],
        [4, 6, 8],
        [2, 5, 5],
    ]
    g = Graph(arr, vertices)
    source = 0
    g.dijkstras_algo(vertices, source)
