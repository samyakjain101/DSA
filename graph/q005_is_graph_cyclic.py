import pathmagic # noqa
from data_structure.graph import Graph as BaseGraph
from queue import Queue


class Graph(BaseGraph):
    def has_cycle(self):
        visited = [False] * len(self.graph)

        for vertex, is_visited in enumerate(visited):
            if not is_visited:

                q = Queue()
                q.put(vertex)

                while q.qsize() > 0:
                    removed = q.get()

                    if visited[removed]:
                        return True

                    visited[removed] = True
                    for edge in self.graph[removed]:
                        if not visited[edge.neighbour]:
                            q.put(edge.neighbour)

        return False


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
    print(g.has_cycle())
