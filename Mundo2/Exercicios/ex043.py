peso = float(input("Digite seu peso: (KG) "))
altura = float(input("Digite sua altura: (M) "))

imc = peso / (pow(altura,2))

if imc < 18.5:
    print(f"Com {imc:.2f} de IMC, você está classificado como ABAIXO DO PESO")

elif imc <= 25:
    print(f"Com {imc:.2f} de IMC, você está classificado como PESO IDEAL")

elif imc <= 30:
    print(f"Com {imc:.2f} de IMC, você está classificado como SOBREPESO")        

elif imc <= 40:
    print(f"Com {imc:.2f} de IMC, você está classificado como OBESIDADE")

else:
    print(f"Com {imc:.2f} de IMC, você está classificado como OBESIDADE MÓRBIDA")
