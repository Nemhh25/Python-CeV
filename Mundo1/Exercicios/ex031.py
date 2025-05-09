distancia = int(input("\033[34mDigite a distância da viagem em KM: \033[m"))
passagem = 0

if distancia <= 200:
    passagem = distancia * 0.50

else:
    passagem = distancia * 0.45

print(f"\033[36mPercorrendo {distancia}KM, a taxa é de R${passagem:.2f}\033[m")    