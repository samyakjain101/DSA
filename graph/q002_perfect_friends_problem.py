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

    def get_connected_component(self):
        visited = [False] * len(self.__graph)

        all_components = []
        for vertex, is_visited in enumerate(visited):
            if not is_visited:
                component = []
                self.__get_connected_component(vertex, visited, component)
                all_components.append(component)

        return all_components

    def __get_connected_component(self, source: int, visited: list, component: list):
        visited[source] = True
        component.append(source)

        for edge in self.__graph[source]:
            if not visited[edge.neighbour]:
                self.__get_connected_component(edge.neighbour, visited, component)


if __name__ == "__main__":
    friends = 7
    k = 5
    arr = [
        [0, 1],
        [2, 3],
        [4, 5],
        [5, 6],
        [4, 6],
    ]
    g = Graph(arr, friends)
    components = g.get_connected_component()

    ways = 0
    i = 0
    j = 1
    while i < len(components):
        while j < len(components):
            ways += len(components[i]) * len(components[j])
            j += 1
        i += 1
        j = i + 1

    print(ways)
