#InterIF 2024 - Fase Local
#Problema I - Boliche

x = int(input())
for _ in range(x):
    player = input()
    partida = input()
    pontuacao = [0]
    i = 0
    while i < len(partida):
        frame = pontuacao[-1]
        if partida[i] == "X":
            frame += 10 + int(partida[i + 1])
            if i < len(partida) - 2: frame += int(partida[i + 2])
            i += 1
        elif i == len(partida) - 1:
            break
        elif int(partida[i]) + int(partida[i + 1]) == 10:
            frame += 10 + int(partida[i + 2])
            i += 2
        else:
            frame += int(partida[i]) + int(partida[i + 1])
            i += 2
        pontuacao.append(frame)
    print(f"{player} : |", end="")
    for i in range(1, len(pontuacao)):
        print(pontuacao[i], end="|")
    print(f" Total = {pontuacao[-1]}")
