
contador = 0
for numero in range(51):
    if numero % 2 == 0:
        print(numero)
        contador += 1

print(f"Quantidade de números pares: {contador}")