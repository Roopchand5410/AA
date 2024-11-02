import numpy as np
from collections import deque

def ford_fulkerson(graph, source, sink):
  vertex_count = len(graph)
  residual_graph = np.copy(graph)
  parent = [-1] * vertex_count
  max_flow = 0

  while bfs(residual_graph, source, sink, parent):
    path_flow = float('inf')
    v = sink
    path_string=" "
    while v != source:
      u = parent[v]
      path_flow = min(path_flow, residual_graph[u][v])
      path_string=f"--> {v}" + path_string
      v = u
    path_string=f"S" + path_string
    print(f"augmentation path:\n{path_string}")
    print(f"bottleneck (min flow added to max flow) = {path_flow}\n")
    v = sink
    while v != source:
      u = parent[v]
      residual_graph[u][v] -= path_flow
      residual_graph[v][u] += path_flow
      v = u
    max_flow += path_flow
  return max_flow
def bfs(residual_graph, source, sink, parent):
  vertex_count = len(residual_graph)
  visited = [False] * vertex_count
  queue = deque([source])
  visited[source] = True
  parent[source] = -1

  while queue:
    u = queue.popleft()
    for v in range(vertex_count):
      if not visited[v] and residual_graph[u][v] > 0:
        queue.append(v)
        parent[v] = u
        visited[v] = True
        if v == sink:
          return True
  return False
graph=[
    [0,10,5,15,0,0,0,0],
    [0,0,4,0,9,15,0,0],
    [0,0,0,4,0,8,0,0],
    [0,0,0,0,0,0,30,0],
    [0,0,0,0,0,15,0,10],
    [0,0,0,0,0,0,15,10],
    [0,0,6,0,0,0,0,10],
    [0,0,0,0,0,0,0,0]
]
source=0
sink=len(graph)-1
max_flow= ford_fulkerson(graph, source, sink)
print(f"Maximum flow:{max_flow}")

'''ouput:augmentation path:
S--> 1--> 4--> 7 
bottleneck (min flow added to max flow) = 9
augmentation path:
S--> 1--> 5--> 7 
bottleneck (min flow added to max flow) = 1
augmentation path:
S--> 2--> 5--> 7 
bottleneck (min flow added to max flow) = 5
augmentation path:
S--> 3--> 6--> 7 
bottleneck (min flow added to max flow) = 10
augmentation path:
S--> 3--> 6--> 2--> 5--> 7 
bottleneck (min flow added to max flow) = 3
Maximum flow:28'''
