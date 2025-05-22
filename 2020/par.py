#InterIF 2020 - Etapa Única
#Problema C - Cadê o meu par?

def calcularDist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

a = int(input())
usuario = [list(map(float, input().split())) for _ in range(a)]
distancia = []
while len(usuario) > 1:
    menor = float('inf')
    for i in range(1, len(usuario)):
        dist = calcularDist(usuario[0], usuario[i])
        if dist < menor:
            menor = dist
            ind = i
    distancia.append(menor)
    usuario.pop(ind)
    usuario.pop(0)

print(f"{sum(distancia):.2f}")
