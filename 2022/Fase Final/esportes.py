#InterIF 2022 - Fase Final
#Problema B - Mapeando Esporte

def dfs(v):
    mark[v] = 1
    for i in g[v]:
        if mark[i] == -1:
            dfs(i)
            
n, m = map(int, input().split())

g = [set() for _ in range(n)]

if n == 2: m = 1

for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].add(v - 1)
    g[v - 1].add(u - 1)

if n == 2:
    print("corrida")
else:
    mark = [-1] * n
    t = 0
    for i in range(n):
        if mark[i] == -1:
            t += 1
            dfs(i)
    if t > 1:
        print("triatlo")
    else:
        print("ciclismo")
