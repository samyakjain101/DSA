class Edge:
    def __init__(self, source=None, neighbour=None):
        self.source = source
        self.neighbour = neighbour


class Graph:
    def __init__(self, graph_array: list, vertices: int):
        self.__graph = [[] for _ in range(vertices)]

        for edge in graph_array:
            vertex1, vertex2 = edge[0], edge[1]
            self.__graph[vertex1].append(Edge(source=vertex1, neighbour=vertex2))
            self.__graph[vertex2].append(Edge(source=vertex2, neighbour=vertex1))

    def get_hamiltonian_paths_and_cycles(self, source: int):
        visited = [False] * len(self.__graph)
        hamil_paths = []
        self.__get_hamil_paths_and_cycles(source, visited, hamil_paths, "")
        return hamil_paths

    def __get_hamil_paths_and_cycles(
        self, source: int, visited: list, hamil_paths: list, path: str
    ):
        if visited[source]:
            return

        visited[source] = True
        path += str(source)

        if len(path) == len(self.__graph):
            hamil_source = int(path[0])
            last_vertex = int(path[-1])

            is_cycle = False
            for edge in self.__graph[last_vertex]:
                if edge.neighbour == hamil_source:
                    is_cycle = True

            if is_cycle:
                path += '*'
            else:
                path += '.'
            hamil_paths.append(path)

        for edge in self.__graph[source]:
            self.__get_hamil_paths_and_cycles(
                edge.neighbour, visited, hamil_paths, path
            )

        visited[source] = False


if __name__ == "__main__":
    vertices = 7
    k = 9

    arr = [
        [0, 1, 10],
        [1, 2, 10],
        [2, 3, 10],
        [0, 3, 10],
        [3, 4, 10],
        [4, 5, 10],
        [5, 6, 10],
        [4, 6, 10],
        [2, 5, 10],
    ]
    source = 0
    g = Graph(arr, vertices)
    print(g.get_hamiltonian_paths_and_cycles(source))
