import re
from collections import deque


# Graph building
# Build graphs using map of form {Vertex: [neighbor_1, ...., neighbor_n]}
def build_graph_part1(filename):
    g = {}
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
    return g


# Graph is built using inverse rules:
# Vertex n's neighbor list consists of bags that can hold n
def build_graph_part2(filename):
    g = {}
    with open(filename) as f:
        for line in f:
            v, w = line.rstrip().split(' bags contain ')
            g[v] = {}
            if w.find('other') > -1:
                continue
            else:
                w = w[:-1].split(', ')
            for color in w:
                color = re.sub(' bag(s)*', '', color)
                quantity = int(color[0])
                color = color[2:]
                g[v][color] = quantity
    return g


# DFS for part 1
def dfs(graph, v, bags):
    bags.add(v)
    if v not in graph:  # Parent bag reached
        return
    for neighbor in graph[v]:
        dfs(graph, neighbor, bags)


# BFS for part 1
def bfs(graph, v, bags):
    q = deque([v])
    while q:
        node = q.popleft()
        if node != 'shiny gold':
            bags.add(node)
        if node not in graph:  # Parent bag found
            continue
        for neighbor in graph[node]:
            q.append(neighbor)


def part2DFS(graph, v):
    total = 0
    for k, val in graph[v].items():
        total += val + (val * part2DFS(graph, k))
    return total


if __name__ == '__main__':
    filename = 'data.txt'
    g_part1 = build_graph_part1(filename)
    g_part2 = build_graph_part2(filename)
    bags = set()
    # BFS from each of shiny gold's neighbors.  Add each encountered bag to the set
    for neighbor in g_part1['shiny gold']:
        dfs(g_part1, neighbor, bags)
    print(
        f'Number of bags that can ultimately hold a "shiny gold" bag: {len(bags)}'
    )
    # recursively add bag contents using DFS
    print(f'One shiny gold bag holds: {part2DFS(g_part2, "shiny gold")}')
