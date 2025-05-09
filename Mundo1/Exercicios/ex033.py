n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor:'))
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')