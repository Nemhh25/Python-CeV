num = 0
contador = 0
soma = 0

num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    
    contador += 1
    soma += num
    num = int(input("Digite um número [999 para parar]: "))
   

print(f"Você digitou {contador} números!")
print(f"A soma é: {soma}")