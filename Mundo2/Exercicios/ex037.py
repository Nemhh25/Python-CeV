numero_inteiro = int(input("Digite um número inteiro: "))

opcoes = int(input("[1] Converter para BINÁRIO \n [2] Converter para octal \n [3] Converter para HEXADECIMAL \n Sua opção: "))

if opcoes == 1:
    print(f"{numero_inteiro} em binário é {bin(numero_inteiro)[2:]}")

elif opcoes == 2:
    print(f"{numero_inteiro} em octal é {oct(numero_inteiro)[2:]}")

elif opcoes == 3:
    print(f"{numero_inteiro} em hexadecimaL é {hex(numero_inteiro)[2:]}")

else:
    print("Opção inválida!")