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
def dfs(i):
    visited[i] = True
    print(i, end=" ")
    for j in range(n):
        if g.graph[i][j] != 0 and visited[j] == False:           
            dfs(j)
starting_point = int(input("Enter starting point of graph: "))
dfs(starting_point)
print()
    