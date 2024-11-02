from queue import Queue
INF = float('inf')
NIL = 0

class BipGraph:
    def __init__(self, m, n):
        self.__m = m
        self.__n = n
        self.__adj = [[] for _ in range(m + 1)]
    
    def addEdge(self, u, v):
        self.__adj[u].append(v)
    
    def bfs(self):
        Q = Queue()
        for u in range(1, self.__m + 1):
            if self.__pairU[u] == NIL:
                self.__dist[u] = 0
                Q.put(u)
            else:
                self.__dist[u] = INF
        self.__dist[NIL] = INF
        
        while not Q.empty():
            u = Q.get()
            if self.__dist[u] < self.__dist[NIL]:
                for v in self.__adj[u]:
                    if self.__dist[self.__pairV[v]] == INF:
                        self.__dist[self.__pairV[v]] = self.__dist[u] + 1
                        Q.put(self.__pairV[v])
        return self.__dist[NIL] != INF
    
    def dfs(self, u):
        if u != NIL:
            for v in self.__adj[u]:
                if self.__dist[self.__pairV[v]] == self.__dist[u] + 1:
                    if self.dfs(self.__pairV[v]):
                        self.__pairV[v] = u
                        self.__pairU[u] = v
                        return True
            self.__dist[u] = INF
            return False
        return True
    
    def hopcroftKarp(self):
        self.__pairU = [NIL] * (self.__m + 1)
        self.__pairV = [NIL] * (self.__n + 1)
        self.__dist = [0] * (self.__m + 1)
        
        result = 0
        while self.bfs():
            for u in range(1, self.__m + 1):
                if self.__pairU[u] == NIL and self.dfs(u):
                    result += 1
        return result

if __name__ == "__main__":
    g = BipGraph(4, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.addEdge(4, 4)
    print("Size of maximum matching is %d" % g.hopcroftKarp())
#ouput:Size of maximum matching is 4
