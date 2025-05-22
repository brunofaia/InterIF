#InterIF 2023 - Fase Final
#Problema G - Lucky Bet Little Tiger Pix

from math import factorial as fact
from math import ceil

def C(n, m):
    return fact(n)//(fact(m) * fact(n - m))

n, cmin, cmax, v = input().split()
n, cmin, cmax = map(int, (n, cmin, cmax))
v = float(v)

base = C(n, cmin)

for i in range(cmin, cmax + 1):
    print(f"Quantidade numeros jogados: {i}")
    print(f"Probabilidade: 1 em {ceil(base/C(i, cmin))}")
    print(f"Probabilidade: {1/ceil(base/C(i, cmin)):.8f} %")
    print(f"Valor aposta: {C(i, cmin)} X R$ {v:.2f} = R$ {C(i, cmin) * v:.2f} ")
    print()
