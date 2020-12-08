import re

class Graph:
    class Vertex:
       def __init__(self):
            self.neighbors = []

    def __init__(self):
        self.vertices = {}


def dfs(graph, v, final, visited):
    global count
    print(f'\tVisiting: {v}')
    # visited[v] = True
    if v == final:
        count += 1
    for neighbor in graph[v]:
        if neighbor == final:
            print(f'\t\tfound: {neighbor} ******************************')
            count += 1
        # if neighbor not in visited:
        return dfs(graph, neighbor, final, visited)
    return 0


if __name__ == '__main__':
    global count
    count = 0
    filename = 'data.txt'
    graph = {}
    # Build graph using map of form {Vertex: [neighbor, .... neighbor]}
    with open(filename) as f:
        graph = {
            y[0]: [
                a[2:]
                for a in re.split(', ', re.sub(' bag(s)*', '', y[1][:-1]))
                if not a[2:].startswith(' other')
            ]
            for y in
            [x.split(' bags contain ') for x in f.read().rstrip().split('\n')]
        }
    for vertex in graph.keys():
        visited = {}
        print(f'starting at: {vertex}')
        dfs(graph, vertex, 'shiny gold', visited)
    print(len(graph.keys()))
    print(graph)
    print(count)
