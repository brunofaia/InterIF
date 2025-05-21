#InterIF 2023 - Fase Local
#Problema D - Jujubas

P = [int(x) for x in input().split()]
N = int(input())
vendas = []
for c in range(N):
  vendas.append([int(x) for x in input().split()])

igualdades = []
for tubos in vendas:
  semelhanca = 0
  for i in range(len(tubos)):
    if tubos[i] == P[i]:
      semelhanca += 1
  igualdades.append(100*(semelhanca/8))

M = int(input())
porcentagens = []
for i in range(M):
  porcentagens.append(int(input()))

for p in porcentagens:
  semelhanca = 0
  for i in igualdades:
    if p <= i: semelhanca += 1
  print(f"{100*(semelhanca / len(igualdades)):.2f}")
