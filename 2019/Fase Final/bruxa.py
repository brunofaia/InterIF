#InterIF 2019 - Fase Final
#Problema G - Bruxa do 171

def dijkstra(u, v):
    dist = [float('inf')] * n
    mark = [-1] * n
    fila = []
    dist[u] = 0
    mark[u] = 1
    fila.append(u)
    while len(fila) > 0:
        atual = min(fila, key = lambda x: dist[x])
        fila.remove(atual)
        weight = dist[atual]
        for i in g[atual]:
            if g[atual][i] + dist[atual] < dist[i]:
                dist[i] = g[atual][i] + dist[atual]
                fila.append(i)
                mark[i] = 1
    return dist[v]

n, m = map(int, input().split())
s, b = map(int, input().split())
g = {i : {} for i in range(n)}
for _ in range(m):
    u, v, d = map(int, input().split())
    g[u][v] = d
    g[v][u] = d

dist = dijkstra(s, b) * 2

print(dist)
