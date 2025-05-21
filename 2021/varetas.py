#InterIF 2021 - Fase Final
#Problema J - Pega Varetas

round = 1
exits = []
while True:
  players = [0, 0, 0]
  N = int(input()) - 1
  if N == -2: break
  V = input().split()
  for i in V:
    if i == "0":
      N += 1
      if N == 3: N = 0
    elif i == "1": players[N] += 5
    elif i == "2": players[N] += 10
    elif i == "3": players[N] += 15
    elif i == "4": players[N] += 20
    elif i == "5": players[N] += 50
  exit = []
  exit.append(f"RODADA {round}")
  winners = []
  for i in range(len(players)):
    if players[i] == max(players): winners.append(f"Jogador {i+1}")
  if len(winners) == 1: exit.append(f"Ganhador com {max(players)} pontos")
  else: exit.append(f"Empate com {max(players)} pontos")
  winners = ", ".join(winners) 
  exit.append(winners)
  exits.append(exit)
  round += 1
for i in exits:
  for j in i:
    print(j)
  if exits.index(i) != len(exits) - 1: print()
