#InterIF 2022 - Fase Final
#Problema G - Teclado

txt = input()
out = []
hist = []

for i in range(len(txt)):
    if txt[i].upper() == "B" and txt[i - 1] == "<" and txt[i + 1] == ">":
        hist.append(out[-1])
        out.pop()
    elif txt[i].upper() == "Z" and txt[i - 1] == "<" and txt[i + 1] == ">":
        if hist[-1] == "-":
            out.pop()
        else:
            out.append(hist[-1])
        hist.pop()
    elif txt[i] not in (">", "<"):
        out.append(txt[i])
        hist.append("-")
        
print("".join(out))
