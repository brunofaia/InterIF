#InterIF 2024 - Fase Local
#Problema H - Ponte que partiu

def dfs(v, g, m):
    m[v] = 1
    for i in g[v]:
        if m[i] == 0:
            dfs(i, g, m)

v = int(input())

g = [set() for _ in range(v)]

aresta = []

for i in range(v):
    i = int(input())
    viz = list(map(int, input().split()))
    for j in viz:
        g[i].add(j)
        g[j].add(i)
        if {i, j} not in aresta:
            aresta.append({i, j})
    
m = [0] * v
t = 0
p = 0

copia = [{j for j in i} for i in g]

for i in range(len(aresta)):
    o, d = aresta[i]
    copia[o].remove(d)
    copia[d].remove(o)
    for j in range(v):
        if m[j] == 0:
            dfs(j, copia, m)
            t += 1
    if t > 1:
        p += 1
    t = 0
    m = [0] * v
    copia = [{j for j in i} for i in g]

print(p)
