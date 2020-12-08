import re

class Graph:

    class Vertex:
        def __init__(self):
            self.neighbors = []

    def __init__(self):
        self.vertices = {}
def dfs(graph, v, final, visited, count):
    visited[v] = True
    if v == final:
        return 1
    for neighbor in graph[v]:
        print(neighbor)
        if neighbor not in visited:
            if neighbor == final:
                return 1
            return dfs(graph, neighbor, final, visited, count)
    return 0


if __name__ == '__main__':
    count = 0
    filename = 'data.txt'
    graph = {}
    # Build graph using map of form {Vertex: [neighbor, .... neighbor]}
    with open(filename) as f:
        graph = {y[0] : [a[2:] for a in re.split(', ', re.sub(' bag(s)*', '', y[1][:-1])) if not a[2:].startswith(' other')] for y in [x.split(' bags contain ') for x in f.read().rstrip().split('\n')]}
    visited = {}
    for vertex in graph.keys():
        count += dfs(graph, vertex, 'shiny gold', visited, count)
    print(count)
