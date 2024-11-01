from collections import deque
def topological_sort(adj, V):
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for adjacent in adj[node]:
            indegree[adjacent] -= 1 
            if indegree[adjacent] == 0:
                q.append(adjacent)
    if len(result) != V:
        print("Graph contains a cycle!")
        return []
    return result
n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]
adj = [[] for _ in range(n)]
for edge in edges:
    adj[edge[0]].append(edge[1])
print("Topological sorting of the graph:", end=" ")
result = topological_sort(adj, n)
for vertex in result:
    print(vertex, end=" ")

#output:Topological sorting of the graph: 0 4 5 1 2 3 
