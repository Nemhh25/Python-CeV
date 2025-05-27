import random
from  time import sleep

numero = list(range(0, 10))

numero_escolhido = random.choice(numero)

print('\033[35m-=-\033[m' * 20)
print('\033[31mVou pensar em um número entre 0 e 10. Tente adivinhar![\033[m')
print('\033[35m-=-\033[m' * 20)

sleep(1)

jogador = int(input("Qual número eu pensei? "))
tentativas = 0

while jogador != numero_escolhido:
    print(f'Você errou! Tente novamente!')
    tentativas += 1
    jogador = int(input("Qual número eu pensei? "))
    
print(f'Parabéns! Você acertou! Demorou um total de {tentativas + 1} tentativas. Eu realmente pensei no {numero_escolhido}')