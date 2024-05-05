from collections import deque
class graph:
    def __init__(self,n):
        self.graph = [[0 for j in range(n)] for i in range(n)]
    def add(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
n = int(input("Enter number of nodes in graph:- "))
g = graph(n)

e = int (input("Enter number of edges in graph:- "))
for i in range(e):
    u, v = map(int, input("Enter Edge(u v):-").split())
    g.add(u, v)

visited = [False]*n
q = deque()
def bfs():
    if not q:
        return
    i = q.popleft()
    print(i, end=" ")
    for j in range(n):
        if g.graph[i][j] != 0 and visited[j] == False:
            q.append(j)
            visited[j] = True  
    bfs()
starting_point = int(input("Enter starting point of graph: "))
visited[starting_point] = True
q.append(starting_point)
bfs()
print()
    