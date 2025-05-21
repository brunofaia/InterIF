#InterIF 2023 - Fase Local
#Problema A - O Bruxo e os Frascos

nome = input()

n_vogais = 0

for x in nome:
  if x.casefold() in 'aeiou':
    n_vogais += 1
    
print('frasco',n_vogais%3)
