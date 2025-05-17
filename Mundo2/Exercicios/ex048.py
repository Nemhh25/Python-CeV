soma = 0
contador = 0

for numeros in range(501):
 
    if numeros % 2 != 0 and numeros % 3 == 0:
       contador +=1
       soma = soma + numeros

print(f"A soma dos {contador} números é {soma}")