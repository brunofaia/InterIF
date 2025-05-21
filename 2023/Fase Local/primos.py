#InterIF 2023 - Fase Local
#Problema C - O Tesouro dos Números Primos

def PrimeNumbers(number):
  global prime_numbers
  prime_numbers = []
  for prime in range(2, number + 1):
    isPrime = True
    for divisor in range(2, int(prime**1/2) + 1):
      if prime % divisor == 0:
        isPrime = False
        break
    if isPrime: prime_numbers.append(prime)
      
n = int(input())
PrimeNumbers(n)

for x in prime_numbers:
  print(x, end=' ')
