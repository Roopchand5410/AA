import heapq

def dijkstra(graph, start):
    dist = {vertex: float('infinity') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    dist[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)
        
        if current_dist > dist[u]:
            continue
        
        for neighbor, weight in graph[u]:
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = u
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist, prev

graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (5, 4), (8, 2)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

start_vertex = 0
distances, predecessors = dijkstra(graph, start_vertex)

print("Distances:", distances)
print("Predecessors:", predecessors)

'''ouput:Distances: {0: 0, 1: 4, 2: 12, 3: 19, 4: 21, 5: 11, 6: 9, 7: 8, 8: 14}
Predecessors: {0: None, 1: 0, 2: 1, 3: 2, 4: 5, 5: 6, 6: 7, 7: 0, 8: 2}'''
