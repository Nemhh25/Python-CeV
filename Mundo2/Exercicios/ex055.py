maior = 0.0
menor = 0.0


for pessoas in range(5):
    peso = float(input(f"Digite o pessoa da pessoa número {pessoas + 1}: "))
    if pessoas == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
             maior = peso
        if peso < menor:
             menor = peso

print(f"O maior peso é: {maior:.2f} e o menor é {menor:.2f}")