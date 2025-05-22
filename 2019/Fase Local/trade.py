#InterIF 2019 - Fase Local
#Problema E - Day Trade

n, p = map(int, input().split())
periodo = [float(input()) for _ in range(p)]
media = []

for i in range(p):
    if i < n - 1:
        media.append(-1)
    else:
        media.append(sum(periodo[i - n + 1:i + 1])/n)
        

c = v = t = 0

for i in range(p - 1):
    if i < n:
        print(i + 1, "Manter", sep=" - ")
    else: 
        if (periodo[i - 1] > media[i - 1] and media[i] > periodo[i]):
            print(i + 1, "Comprar", sep=" - ")
            t -= periodo[i]
            c += 1
        elif (media[i - 1] > periodo[i - 1] and periodo[i] > media[i]):
            print(i + 1, "Vender", sep=" - ")
            t += periodo[i]
            v += 1
        else:
            print(i + 1, "Manter", sep=" - ")

if c > v:
    print(n, "Vender", sep=" - ")
    t += periodo[p - 1]
elif v > c:
    print(n, "Comprar", sep=" - ")
    t -= periodo[p - 1]
else:
    print(n, "Manter", sep=" - ")
    
print(f"{t:.2f}")
