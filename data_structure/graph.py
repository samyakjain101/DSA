class Edge:
    def __init__(self, source: int, neighbour: int, weight: int):
        self.source = source
        self.neighbour = neighbour
        self.weight = weight


class Graph:
    def __init__(self, graph_array):
        """Takes in 2-D array

        example-
        :graph_array: [[source, destination, weight], ...]
        Source and destination value should be less than len(graph_array)
        and greater than or equal to zero.

        """
        self.build_graph(graph_array)

    graph = None

    def build_graph(self, graph_array: list):
        graph = [[] for _ in range(len(graph_array))]

        for edge in graph_array:
            vertex1: int = edge[0]
            vertex2: int = edge[1]
            weight: int = edge[2]

            graph[vertex1].append(
                Edge(source=vertex1, neighbour=vertex2, weight=weight)
            )
            graph[vertex2].append(
                Edge(source=vertex2, neighbour=vertex1, weight=weight)
            )

        self.graph = graph

    def hasPath(self, source: int, destination: int) -> bool:
        visited = [False] * len(self.graph)
        return self.__hasPath(source, destination, visited)

    def __hasPath(self, source: int, destination: int, visited: list) -> bool:
        if source == destination:
            return True

        if not visited[source]:
            visited[source] = True

            for edge in self.graph[source]:
                if self.__hasPath(edge.neighbour, destination, visited):
                    return True

        return False


if __name__ == "__main__":
    g = Graph(
        [
            [0, 1, 10],
            [1, 2, 10],
            [2, 3, 10],
            [0, 3, 10],
            [3, 4, 10],
            [4, 5, 10],
            [5, 6, 10],
            [4, 6, 10],
        ]
    )
    print(g.hasPath(0, 6))
