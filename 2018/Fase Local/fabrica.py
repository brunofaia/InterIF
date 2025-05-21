#InterIF 2018 - Fase Local
#Problema D - Fábrica de Automóveis

m, q = map(int, input().split())
parafuso = list(map(int, input().split()))
trava = list(map(int, input().split()))
peca = [parafuso] + [trava]
mes = [list(map(int, input().split())) for _ in range(m)]
tabela = [[0] * q for _ in range(2)]

for i in range(2):
    for k in range(q):
        for j in range(m):
            tabela[i][k] += peca[i][j] * mes[j][k]
            
for i in tabela:
    for j in i:
        print(j, end="\t")
    print()
