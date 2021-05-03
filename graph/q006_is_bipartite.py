from queue import Queue


class Edge:
    def __init__(self, src=None, nbr=None):
        self.src = src
        self.nbr = nbr


class Pair:
    def __init__(self, vertex: int, psf: str):
        self.vertex = vertex
        self.psf = psf


class Graph:
    def __init__(self, graph_arr: list, vertices: int):
        self.graph = [[] for _ in range(vertices)]

        for edge in graph_arr:
            v1, v2, _ = edge
            e1 = Edge(src=v1, nbr=v2)
            e2 = Edge(src=v2, nbr=v1)

            self.graph[v1].append(e1)
            self.graph[v2].append(e2)

    def is_bipartite(self):
        visited = [False] * len(self.graph)

        for vertex, is_visited in enumerate(visited):
            if is_visited:
                continue

            q = Queue()
            q.put(Pair(vertex=vertex, psf=f"{vertex}"))

            while q.qsize():
                removed = q.get()

                if visited[removed.vertex]:
                    # count psf length
                    if len(removed.psf) % 2 != 0:
                        # Odd length => Not Bipartite
                        return False

                visited[removed.vertex] = True
                for edge in self.graph[removed.vertex]:
                    if not visited[edge.nbr]:
                        q.put(Pair(vertex=edge.nbr, psf=f"{removed.psf}{edge.nbr}"))

        # Acyclic => Bipartite
        # OR all cycles even length => Bipartie
        return True


if __name__ == "__main__":
    vertices = 7
    k = 8
    arr= [
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
    print(g.is_bipartite())
