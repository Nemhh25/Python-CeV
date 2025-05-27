media = 0.0
maior = 0
menor_20 = 0
somaidade = 0
nomevelho = ""

for i in range(4):

    print(f"---- PESSOA {i+1} ----")
    nome = input("Digite o nome da pessoa: ").strip()
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa: [M/F] ").strip()
    somaidade += idade

    if i == 0 and sexo in "Mm":
        maior = idade
        nomevelho = nome

    if sexo in "Mm" and idade > maior:
        maior = idade
        nomevelho = nome
    
    if sexo in "Ff" and idade < 20:
        menor_20 += 1

media = somaidade / 4

print(f"A média de idade do grupo é de {media}")
print(f"O homem mais velho é {nomevelho} e ele tem {maior} anos")
print(f"Há um total de {menor_20} mulheres com idade inferior à 20 anos.")