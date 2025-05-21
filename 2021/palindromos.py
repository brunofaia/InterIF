#InterIF 2021 - Fase Final
#Problema B - Otto e seus palíndromos

S = input().lower()
letras = {}
for ch in S:
  if ch == ' ': continue
  if ch not in letras:
    letras[ch] = 1
    continue
  letras[ch] += 1
impar = 0
for ch in letras:
  if letras[ch] % 2 == 1: impar += 1
if impar > 1: print(0)
else: print(1)
