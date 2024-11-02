from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        stack.append(v)

    def _transpose(self):
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def _fill_order(self, visited, stack):
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)

    def _dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, component)

    def kosaraju_scc(self):
        stack = deque()
        visited = [False] * self.V

        # Fill stack with vertices based on their finishing order
        self._fill_order(visited, stack)

        # Get the transposed graph
        transposed_graph = self._transpose()

        # Mark all vertices as not visited for the second DFS
        visited = [False] * self.V
        scc_list = []

        # Process vertices in order defined by the stack
        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                scc_list.append(component)

        return scc_list

# Example usage
g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 7)
g.add_edge(6, 5)
g.add_edge(7, 6)

sccs = g.kosaraju_scc()
print("Strongly Connected Components:", sccs)

#output:Strongly Connected Components: [[0, 2, 1], [4], [5, 6, 7], [3]]
