#InterIF 2018 - Fase Final
#Problema H - Círculo da Morte

n = int(input())
x = int(input())
roda = list(range(1, n + 1))

p = True
j = 0
i = 1

while roda.count(0) < len(roda) - 1:
    if p and roda[i % n]:
        j += 1
        if j == x:
            print(f"Morte {j}: {roda[i % n]}")
        roda[i % n] = 0
        p = False
    elif roda[i % n]:
        p = True
    i += 1
    
for i in roda:
    if i: print(f"Sobrevivente: {i}")
