#InterIF 2019 - Fase Final
#Problema F - Bordando em Ponto Cruz

digitos = {
    "0": (" XX ", "X  X", "X  X", "X  X", "X  X", "X  X", " XX "),
    "1": ("  XX", " X X", "X  X", "   X", "   X", "   X", "   X"),
    "2": (" XX ", "X  X", "   X", "  X ", " X  ", "X   ", "XXXX"),
    "3": ("XXX ", "   X", "   X", "XXX ", "   X", "   X", "XXX "),
    "4": ("X  X", "X  X", "X  X", "XXXX", "   X", "   X", "   X"),
    "5": ("XXXX", "X   ", "X   ", "XXX ", "   X", "   X", "XXX "),
    "6": (" XXX", "X   ", "X   ", "XXX ", "X  X", "X  X", " XX "),
    "7": ("XXXX", "   X", "   X", "  X ", " X  ", "X   ", "X   "),
    "8": (" XX ", "X  X", "X  X", " XX ", "X  X", "X  X", " XX "),
    "9": (" XX ", "X  X", "X  X", " XXX", "   X", "   X", "XXX "),
    ".": (" ", " ", " ", " ", " ", "X", "X")
}

data = input()

line = [""] * 7

for i in data:
    char = digitos[i]
    for j in range(7):
        line[j] += char[j] + "  "

for i in line:
    print(i)
