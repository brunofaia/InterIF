#InterIF 2019 - Fase Local
#Problema C - Achando a figurinha

from math import ceil

n = int(input())
fig = [int(input()) for _ in range(n)]
for i in fig:
    pag = ceil(i / 9)
    p = i - (pag - 1) * 9
    if p % 3 == 0: c = 3
    else: c = p % 3
    l = ceil(p / 3)
    print(pag, l, c)
