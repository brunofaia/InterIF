#InterIF 2019 - Fase Local
#Problema A - Começando a Investir

v = float(input())
n = int(input())
nota = []
total = 0
for _ in range(n):
    c, q, p = input().split()
    q = int(q)
    p = float(p)
    nota.append([c, q, p, q * p])
    total += nota[-1][-1]

taxa = total * 0.000275 + total * 0.00005 + n * v

for i in range(n):
    nota[i][-1] += nota[i][-1]/total * taxa
    nota[i][-2] = nota[i][-1] / nota[i][-3]
    
for i in range(n):
    print(f"{nota[i][0]} {nota[i][1]} {nota[i][2]:.2f} {nota[i][3]:.2f}")
    
print(f"{total:.2f}")
print(f"{taxa:.2f}")
