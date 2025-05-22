#InterIF 2020 - Etapa Única
#Problema G - Rede

def dfs(v):
    mark[v] = 1
    for i in g[v]:
        if mark[i] == -1:
            dfs(i)
            
n, m = map(int, input().split())
g = [[] for _ in range(n)]
e = []

s = 0

for _ in range(m):
    u, v, d = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
    s += d
    e.append([u - 1, v - 1, d])

e.sort(reverse = True, key = lambda x: x[2])

for i in range(m):
    u, v, d = e[i]
    g[u].remove(v)
    g[v].remove(u)
    mark = [-1] * n
    t = 0
    for j in range(n):
        if mark[j] == -1:
            dfs(j)
            t += 1
    if t > 1:
        g[u].append(v)
        g[v].append(u)
    else:
        s -= d

print(s)
