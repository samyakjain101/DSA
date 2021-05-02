class Edge:
    def __init__(self, source: int, neighbour: int, weight: int):
        self.source = source
        self.neighbour = neighbour
        self.weight = weight


class Graph:
    def __init__(self, graph_array: list, vertices: int):
        """Takes in 2-D array

        example-
        :graph_array: [[source, destination, weight], ...]
        Source and destination value should be less than len(graph_array)
        and greater than or equal to zero.

        """
        self.build_graph(graph_array, vertices)

    graph = None

    def build_graph(self, graph_array: list, vertices: int):
        graph = [[] for _ in range(vertices)]

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

    def allPath(self, source: int, destination: int) -> None:
        visited = [False] * len(self.graph)
        return self.__allPath(source, destination, visited, "")

    def __allPath(self, source: int, destination: int, visited: list, path: str):
        if source == destination:
            path += str(destination)
            print(path)
            return

        if not visited[source]:
            visited[source] = True
            path += str(source)

            for edge in self.graph[source]:
                self.__allPath(edge.neighbour, destination, visited, path)

            visited[source] = False

    def multisolver(self, source: int, destination: int, criteria: int, k: int):
        visited = [False] * len(self.graph)
        return self.__multisolver(source, destination, visited, "", 0, criteria, k)

    smallest_path = None
    smallest_path_weight = float("inf")
    longest_path = None
    longest_path_weight = float("-inf")

    just_larger_path = None
    just_larger_path_weight = float("inf")
    just_smaller_path = None
    just_smaller_path_weight = float("-inf")

    def __multisolver(
        self,
        source: int,
        desination: int,
        visited: list,
        path: str,
        weight: int,
        criteria: int,
        k: int,
    ):
        if source == desination:
            path += str(desination)

            if weight < self.smallest_path_weight:
                self.smallest_path = path
                self.smallest_path_weight = weight

            if weight > self.longest_path_weight:
                self.longest_path = path
                self.longest_path_weight = weight

            if criteria < weight < self.just_larger_path_weight:
                self.just_larger_path = path
                self.just_larger_path_weight = weight

            if criteria > weight > self.just_smaller_path_weight:
                self.just_smaller_path = path
                self.just_smaller_path_weight = weight

            return

        if not visited[source]:
            visited[source] = True
            path += str(source)

            for edge in self.graph[source]:
                self.__multisolver(
                    edge.neighbour,
                    desination,
                    visited,
                    path,
                    weight + edge.weight,
                    criteria,
                    k,
                )

            visited[source] = False

    def get_connected_components(self):
        visited = [False] * len(self.graph)
        paths = []
        for idx, value in enumerate(visited):
            if not value:
                path = []
                self.__get_connected_components(idx, visited, path)
                paths.append(path)
        return paths

    def __get_connected_components(self, source: int, visited: list, path: list):
        path.append(source)
        visited[source] = True

        for edge in self.graph[source]:
            if not visited[edge.neighbour]:
                self.__get_connected_components(edge.neighbour, visited, path)

    def is_connected(self):
        return len(self.get_connected_components()) == 1


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
        ],
        7,
    )
    # g.allPath(0, 6)
    # g = Graph([[0, 1, 10], [2, 3, 10], [4, 5, 10], [5, 6, 10], [4, 6, 10]], 7)
    print(g.get_connected_components())
    print(g.is_connected())
