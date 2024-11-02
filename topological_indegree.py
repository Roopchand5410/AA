from collections import deque

def topological_sort(v, adj):
    indegree = [0] * v

    for i in range(v):
        for vertex in adj[i]:
            indegree[vertex] += 1

    q = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    res = []

    while q:
        node = q.popleft()
        res.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if len(res) != v:
        return []
    else:
        return res

n = 6
edges = [[0, 1], [0, 4], [4, 5], [1, 2], [5, 2], [2, 3]]
adj = [[] for _ in range(n)]
for edge in edges:
    adj[edge[0]].append(edge[1])

print(topological_sort(n, adj))
#ouput:[0,4,5,1,2,3]
