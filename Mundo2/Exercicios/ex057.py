sexo = input("Digite o sexo: [M/F/NB]").upper()

while sexo not in "MF":
    print("Sexo inválido, digite novamente!") 
    sexo = input("Digite o sexo: [M/F/NB]").upper()

print(f"O sexo é {sexo}")