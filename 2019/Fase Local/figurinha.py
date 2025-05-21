#InterIF 2019 - Fase Final
#Problema A - Figurinhas - Parte 2

price = float(input()[2:])
coins = [0.25, 0.1, 0.05, 0.01]
number_coins = [int(x) for x in input().split()]
cards = 0
pay = 0
while sum([a * b for a, b in zip(coins, number_coins)]) >= price:
  for i in range(len(coins)):
    while pay < price and number_coins[i] > 0:
      pay += coins[i]
      number_coins[i] -= 1
    if pay >= price:
      cards += int(pay//price)
      pay %= price
      break
print(cards)
print(sum(number_coins))
