import heapq
import math

# ---------------------------
# 1. Dijkstra's Algorithm
# ---------------------------
def dijkstra(graph, source):
    dist = {node: math.inf for node in graph}
    dist[source] = 0
    heap = [(0, source)]
    
    while heap:
        curr_dist, u = heapq.heappop(heap)
        if curr_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    
    return dist

# Example graph from CLRS (Figure 24.6, Page 662):
example_graph_dijkstra = {
    's': [('t', 10), ('y', 5)],
    't': [('x', 1), ('y', 2)],
    'x': [('z', 4)],
    'y': [('t', 3), ('x', 9), ('z', 2)],
    'z': [('s', 7), ('x', 6)]
}

print("Dijkstra's Algorithm (from 's'):")
distances = dijkstra(example_graph_dijkstra, 's')
for node, d in distances.items():
    print(f"Distance to {node}: {d}")
print()

# ---------------------------
# 2. Bellman-Ford Algorithm
# ---------------------------
def bellman_ford(edges, vertices, source):
    dist = {v: math.inf for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise Exception("Graph contains a negative-weight cycle")

    return dist

# Example graph from CLRS (Figure 24.4, Page 659):
example_edges_bellman_ford = [
    ('s', 't', 6),
    ('s', 'y', 7),
    ('t', 'x', 5),
    ('t', 'y', 8),
    ('t', 'z', -4),
    ('x', 't', -2),
    ('y', 'x', -3),
    ('y', 'z', 9),
    ('z', 'x', 7),
    ('z', 's', 2)
]
vertices_bf = ['s', 't', 'x', 'y', 'z']

print("Bellman-Ford Algorithm (from 's'):")
distances = bellman_ford(example_edges_bellman_ford, vertices_bf, 's')
for node, d in distances.items():
    print(f"Distance to {node}: {d}")
print()

# ---------------------------
# 3. Floyd-Warshall Algorithm
# ---------------------------
def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {u: {v: math.inf for v in nodes} for u in nodes}
    
    for u in nodes:
        dist[u][u] = 0
        for v, w in graph[u]:
            dist[u][v] = w

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example graph from CLRS (Figure 25.1, Page 693):
example_graph_fw = {
    '1': [('2', 3), ('3', 8), ('5', -4)],
    '2': [('5', 7), ('4', 1)],
    '3': [('2', 4)],
    '4': [('3', -5), ('1', 2)],
    '5': [('4', 6)]
}

print("Floyd-Warshall Algorithm (All-pairs shortest paths):")
distances = floyd_warshall(example_graph_fw)
for u in distances:
    for v in distances[u]:
        d = distances[u][v]
        d_str = f"{d}" if d != math.inf else "INF"
        print(f"Shortest path {u} → {v}: {d_str}")
print()
