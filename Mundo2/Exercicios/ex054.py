maior_1idade = 0
menor_idade = 0


for i in range(7):
    idade = int(input(f"Digite a idade da pessoa número {i + 1}: "))
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"Total de pessoas maior de idade = {maior_idade}")
print(f"Total de pessoas menor de idade = {menor_idade}")