from collections import defaultdict, deque
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    bfs_result = g.bfs(0)
    print("BFS Traversal:", bfs_result)

#ouput:BFS Traversal: [0, 1, 2, 3, 4, 5]
