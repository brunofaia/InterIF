#InterIF 2023 - Fase Local
#Problema B - Classificação para corrida de kart

a,b,c = [int(x) for x in input().split()]
players = []
for x in range(a):
  p = input()
  players.append(p)
laps = []
for x in range(b):
  l = input()
  laps.append(l)
for x in range(c):
  il = input()
  laps.remove(il)
laps_time = []
for x in laps:
  t = x.split()[1].replace(':',' ').replace('.', ' ').split()
  t = int(t[0])+int(t[1])/60+int(t[2])/1000
  laps_time.append(t)
for x in range(a):
  racer = laps[laps_time.index(min(laps_time))]
  for p in players:
    if p[:3].upper() == racer[:3]: print(x+1,racer.replace(racer[:3], p))
  laps_time = [laps_time[i] for i in range(len(laps)) if racer[:3] not in laps[i]]
  laps = [lap for lap in laps if racer[:3] not in lap]
