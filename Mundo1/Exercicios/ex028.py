import random
from time import sleep


numero = [0, 1, 2, 3 , 4, 5]

numero_escolhido = random.choice(numero)

print('\033[35m-=-\033[m' * 20)
print('\033[31mVou pensar em um número entre 0 e 5. Tente adivinhar![\033[m')
print('\033[35m-=-\033[m' * 20)

jogador = int(input('Qual número eu pensei? '))

print('\033[35m-=-\033[m' * 20)
sleep(2)

print('\033[36m Processando... \033[m')
if jogador == numero_escolhido:
    print('Parabéns! Você acertou!')

else:
    print(f'Você errou! Eu pensei no número {numero_escolhido} e não no {jogador}.')

print('\033[35m-=-\033[m' * 20)