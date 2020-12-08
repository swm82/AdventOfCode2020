import re

def dfs(graph, v, bags):
    bags.add(v)
    if v not in graph:  # Parent bag reached
        return
    for neighbor in graph[v]:
        dfs(graph, neighbor, bags)


if __name__ == '__main__':
    filename = 'data.txt'
    g = {}
    # Build graph using map of form {Vertex: [neighbor_1, ...., neighbor_n]}
    # Graph is built using inverse rules:
    # Vertex n's neighbor list consists of bags that can hold n
    with open(filename) as f:
        for line in f:
            v, w = line.rstrip().split(' bags contain ')
            if w.find('other') > -1:
                w = []
            else:
                w = re.split(',', re.sub('( bag(s)*|( )*(\d)+ )', '', w[:-1]))
            for color in w:
                if color not in g:
                    g[color] = [v]
                else:
                    g[color].append(v)
    bags = set()
    # DFS from each of shiny gold's neighbors.  Add each encountered bag to the set
    for neighbor in g['shiny gold']:
        dfs(g, neighbor, bags)
    print(bags)
    print(
        f'Number of bags that can ultimately hold a "shiny gold" bag: {len(bags)}'
    )
