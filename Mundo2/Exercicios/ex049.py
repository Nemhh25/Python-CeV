tabuada = int(input("Qual tabuada você deseja? "))
fim = int (input("Quantas vezes? "))

for i in range(0, fim+1, 1):
    print(f"{tabuada} * {i} = {tabuada * i}")