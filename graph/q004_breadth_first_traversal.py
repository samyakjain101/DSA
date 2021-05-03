import pathmagic  # noqa
from queue import Queue
from data_structure.graph import Graph as GenericGraph


class Pair:
    def __init__(self, vertex: int, psf: str):
        # psf: path so far
        self.vertex = vertex
        self.psf = psf


class Graph(GenericGraph):
    def bfs(self, source: int):
        visited = [False] * len(self.graph)
        q = Queue()

        q.put(Pair(vertex=source, psf=str(source)))

        while q.qsize():
            removed = q.get()

            if visited[removed.vertex]:
                continue

            visited[removed.vertex] = True
            print(f'{removed.vertex}@{removed.psf}')

            for edge in self.graph[removed.vertex]:
                if not visited[edge.neighbour]:
                    q.put(Pair(vertex=edge.neighbour, psf=removed.psf + str(edge.neighbour)))


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
    source = 2
    g = Graph(arr, vertices)
    g.bfs(source)
