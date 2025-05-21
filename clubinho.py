#Problema H - Clubinho da Isa

N = [int(input()) for i in range(4)]

sorted_N = sorted(N)

if N[0] + N[1] + N[2] == N[3] and sorted_N == N:
  print("LIBERADO")

else: print("NEGADO")
