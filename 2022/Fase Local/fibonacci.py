#InterIF 2022 - Fase Local
#Problema D - Fibonacci

def isFibo(s):
    if s[0] != 1 or s[1] != 1:
        return False
    for i in range(len(s) - 2):
        if s[i] + s[i + 1] != s[i + 2]:
            return False
    return True

def main():
    n = int(input())
    matriz = [list(map(int, input().split())) for _ in range(n)]
    fibo = []
    for i in range(n//2 + 1):
        borda = matriz[i][i:n-i] + matriz[n-i-1][i:n-i]
        for j in range(1 + i, n - i - 1):
            borda += [matriz[j][i]]
            borda += [matriz[j][n-i-1]]
        if len(set(borda)) != 1:
            print("Nao fibonnaci")
            return
        fibo.append(borda[0])
    fibo = fibo[::-1]
    if isFibo(fibo):
        print("Fibonnaci")
    else:
        print("Nao fibonnaci")

main()
