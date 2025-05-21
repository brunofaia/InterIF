#InterIF 2023 - Fase Local
#Problema E - Alguém ainda sabe o que é um cheque?

N = int(input()) 
notas = [] 
for i in range(N): notas.append(int(input())) 
notas.sort(reverse=True)
V = int(input())
n_cedulas = 0
for nota in notas:
  while (V - nota) >= 0:
    V -= nota
    n_cedulas += 1
print(n_cedulas)
