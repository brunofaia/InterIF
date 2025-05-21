#InterIF 2023 - Fase Local
#Problema F - Cavalinhos do Recantão

class Time:
  def __init__(self, nome):
    self.nome = nome
    self.pontos = 0
    self.vitorias = 0
    self.gols = 0
    self.golsSofridos = 0

  def __str__(self):
    return f"{self.nome} {self.pontos} {self.vitorias} {self.gols - self.golsSofridos}"
    
  def venceu(self):
    self.pontos += 3
    self.vitorias += 1

  def empate(self):
    self.pontos += 1

  def gol(self, gols, golsSofridos):
    self.gols += gols
    self.golsSofridos += golsSofridos

E = int(input())
N = int(input())
times = {}
for i in range(N):
  linha = [x for x in input().split()]
  if linha[0] not in times:
    times[linha[0]] = Time(linha[0])

  if linha[4] not in times:
    times[linha[4]] = Time(linha[4])

  if linha[1] > linha[3]:
    times[linha[0]].venceu()
    times[linha[0]].gol(int(linha[1]), int(linha[3]))
    times[linha[4]].gol(int(linha[3]), int(linha[1]))

  elif linha[1] == linha[3]:
    times[linha[0]].empate()
    times[linha[4]].empate()
    times[linha[0]].gol(int(linha[1]), int(linha[3]))
    times[linha[4]].gol(int(linha[3]), int(linha[1]))

  else:
    times[linha[4]].venceu()
    times[linha[4]].gol(int(linha[3]), int(linha[1]))
    times[linha[0]].gol(int(linha[1]), int(linha[3]))

sortedlist = sorted(times, reverse=True, key=lambda x: (times[x].pontos, times[x].vitorias, (times[x].gols - times[x].golsSofridos)))

for time in sortedlist:
  print(times[time])
