resp = "S"
cont = 0
media = 0
maior = 0
menor = 0
soma = 0


while resp in "Ss":
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        
        if num < menor:
            num = menor
            
    resp = input("Quer continuar? [S/N] ").upper().strip()[0]


media = soma / cont
print(f"Você digitou {cont} números e a média foi {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")

    
    
    