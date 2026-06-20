class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if not src in self.adjList:
            self.adjList[src] = []
        if not dst in self.adjList:
            self.adjList[dst] = []
        srcNeighbors = self.adjList[src]
        if not dst in srcNeighbors:
            srcNeighbors.append(dst)
        print(self.adjList)

    def removeEdge(self, src: int, dst: int) -> bool:
        if not src in self.adjList:
            return False
        srcNeighbors = self.adjList[src]
        if dst in srcNeighbors:
            srcNeighbors.remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if not src in self.adjList:
            return False
        
        queue = deque([src])
        visited = set([src])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                
                for neighbor in self.adjList[node]:
                    if neighbor != src and not neighbor in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        
        return False

        