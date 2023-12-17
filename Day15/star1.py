sampleData = \
"""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

data = open('data.txt', 'r', encoding="utf-8").read()
# data = sampleData

def dijkstra(graph: dict, start: str):
    dist, prev = {}, {}
    result = []

    for vertice in graph:
        dist[vertice] = float('inf')
        prev[vertice] = None
    dist[start] = 0

    Q = [vertice for vertice in graph]

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)
        result.append(u)

        for neighbor in graph[u]:
            if neighbor in Q and dist[neighbor] > dist[u] + graph[u][neighbor]:
                dist[neighbor] = dist[u] + graph[u][neighbor]
                prev[neighbor] = u
    
    return result, dist, prev


matrix = [[int(digit) for digit in line] for line in data.split('\n')]

graph = dict()
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        graph[f'{x},{y}'] = dict()
        if y > 0:
            graph[f'{x},{y}'][f'{x},{y-1}'] = matrix[y-1][x]
        if y < len(matrix) - 1:
            graph[f'{x},{y}'][f'{x},{y+1}'] = matrix[y+1][x]
        if x > 0:
            graph[f'{x},{y}'][f'{x-1},{y}'] = matrix[y][x-1]
        if x < len(matrix[0]) - 1:
            graph[f'{x},{y}'][f'{x+1},{y}'] = matrix[y][x+1]
# print(graph)

s, distance, previous = dijkstra(graph, '0,0')
print(distance[f'{len(matrix)-1},{len(matrix)-1}'])
