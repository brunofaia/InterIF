#InterIF 2019 - Fase Local
#Problema F - Há Caminho Para Birigui?

def dfs(v):
    for i in g[v]:
        if mark[i] == -1:
            mark[i] = 1
            dfs(i)

n, m = map(int, input().split())
s, b = map(int, input().split())

g = [[] for _ in range(n)]
mark = [-1] * n

for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

mark[s - 1] = 1
dfs(s - 1)

if mark[b - 1] == -1:
    print("NAO EXISTE CAMINHO")
else:
    print("HA CAMINHO ATE BIRIGUI")
