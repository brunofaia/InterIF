#InterIF 2022 - Fase Local
#Problema F - Passeio no parque

#Caminho Euleriano é aquele que utiliza as arestas do grafo uma única vez
#Para um caminho ser Euleriano, o grafo tem de possuir exatamente 0 ou 2 vizinhos que possuam ímpar vízinhos

n = int(input()) #total de arestas

grafo = [0 for _ in range(n)] #total de vizinhos de cara aresta

for _ in range(n): #recebendo arestas
    o, d = map(int, input().split())
    grafo[o] += 1
    grafo[d] += 1
    
t = 0

for i in grafo: #contando quantos vértices tem ímpar vizinhos
    if i % 2 == 1:
        t += 1

if t == 0 or t == 2:
    print("Sim")
else:
    print("Nao")
