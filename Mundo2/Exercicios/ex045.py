from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("""Suas opções: 
[1] Pedra
[2] Papel
[3] Tesoura """)

jogador = int(input("Qual é sua jogada? "))

print(f"O jogador escolheu {itens[jogador]}")
print(f"O computador escolheu {itens[computador]}")

if jogador == computador:
    print("EMPATE!")

elif jogador == 1 and computador == 2:
    print("COMPUTADOR VENCE!")
elif jogador == 1 and computador == 0:
    print("JOGADOR VENCE!")
elif jogador == 2 and computador == 0:
    print("COMPUTADOR VENCE!")
elif jogador == 2 and computador == 1:
    print("JOGADOR VENCE!")
elif jogador == 3 and computador == 1:
    print("COMPUTADOR VENCE!")
elif jogador == 3 and computador == 2:
    print("JOGADOR VENCE!")
else:
    print("Jogada inválida!")

