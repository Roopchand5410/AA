from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    def dfs(self, start):
        visited = set()
        result = []
        self.dfs_util(start, visited, result)
        return result
    def dfs_util(self, node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    dfs_result = g.dfs(0)
    print("DFS Traversal:", dfs_result)

#output:DFS Traversal: [0, 1, 3, 5, 4, 2]
