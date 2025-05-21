#InterIF 2021 - Fase Final
#Problema D - Problema de Syracuse

while True:
  try:
    P = 0
    N = int(input())
    while N != 1:
      if N % 2 == 0: N //= 2
      else: N = 3*N + 1
      P += 1
    print(P)
  except EOFError:
    break
