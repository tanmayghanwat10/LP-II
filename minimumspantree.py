import random
class graph:
    def __init__(self,n):
        self.graph = [[ float('inf') for j in range(n)] for i in range(n)]
    def add(self,u,v, w):
        self.graph[u][v] = w
        self.graph[v][u] =  w


n = int(input("Enter number of nodes in graph:- "))
g = graph(n)

e = int (input("Enter number of edges in graph:- "))
for i in range(e):
    u, v, w = map(int, input("Enter Edge(u v w):-").split()) 
    g.add(u, v, w)

starting_point = random.randint(0, n - 1)
print(f"Starting Point : {starting_point}")
visited = [starting_point]
ans = []
while len(visited) < n:
    mini = float("inf")
    for i in visited:
        for j in range(n):
            weight = g.graph[i][j]
            if j not in visited and weight < mini:
                mini = weight
                temp = (i, j, weight)
    
    ans.append(temp)
    visited.append(temp[1])

for edge in ans:
    print(f"{edge[0]} - {edge[1]} -> {edge[2]}")