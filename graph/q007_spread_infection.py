from queue import Queue


class Edge:
    def __init__(self, src=None, nbr=None):
        self.src = src
        self.nbr = nbr


class Pair:
    def __init__(self, vertex: int, time: int):
        self.vertex = vertex
        self.time = time


class Graph:
    def __init__(self, graph_arr: list, vertices: int):
        self.graph = [[] for _ in range(vertices)]

        for edge in graph_arr:
            v1, v2, _ = edge
            e1 = Edge(src=v1, nbr=v2)
            e2 = Edge(src=v2, nbr=v1)

            self.graph[v1].append(e1)
            self.graph[v2].append(e2)

    def spread_infection(self, source: int, time: int):
        visited = [False] * len(self.graph)

        q = Queue()
        q.put(Pair(vertex=source, time=1))

        count = 0
        while q.qsize():
            removed = q.get()

            if removed.time > time:
                break

            if not visited[removed.vertex]:
                visited[removed.vertex] = True
                count += 1

                for edge in self.graph[removed.vertex]:
                    if not visited[edge.nbr]:
                        q.put(Pair(vertex=edge.nbr, time=removed.time + 1))

        return count


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
    source = 6
    time = 3
    g = Graph(arr, vertices)
    print(g.spread_infection(source, time))
