#InterIF 2019 - Fase Final
#Problema C - Dança das Cadeiras

n, p = map(int, input().split())
partido = [int(input()) for _ in range(p)]

qe = sum(partido)/n
if qe % 1 > 0.5: qe += 1
qe = int(qe)

cadeira = [i//qe for i in partido]

sobras = n - sum(cadeira)
for _ in range(sobras):
    vaga = [partido[i]//(cadeira[i] + 1) for i in range(p)]
    cadeira[vaga.index(max(vaga))] += 1

for i in cadeira: print(i)
