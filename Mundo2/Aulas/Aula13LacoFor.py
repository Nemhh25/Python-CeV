for c in range(0, 10, 2): # 0 é o inicio, 10 é o fim e 2 é o passo
    print(c) # printa o valor de c
print('Fim') 

for c in range(6, 0, -1): # 6 é o inicio, 0 é o fim e -1 é o passo
    print(c) # printa o valor de c
print('Fim')

for c in range(0, 10, 3): # 0 é o inicio, 10 é o fim e 3 é o passo
    print(c) # printa o valor de c
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1): # 0 é o inicio, n+1 é o fim e 1 é o passo
    print(c) # printa o valor de c
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # i é o inicio, f+1 é o fim e p é o passo
    print(c) # printa o valor de c
print('Fim')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma de todos os valores foi {s}')











