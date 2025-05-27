import random
from time import sleep

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

aleatorio1 = random.randint(0, 10000)
aleatorio2 = random.randint(0, 10000)

soma = n1 + n2
multiplicacao = n1 * n2
maior = 0.0
resultado = 0.0

print('\033[35m-=-\033[m' * 20)
print("""[1] Somar
[2] Multiplicar
[3] Verificar o maior
[4] Novos números 
[5] Sair do programa""")
opcao = int(input('\033[36mO que você deseja fazer? \033[m' ))



while True:
    if opcao == 1:
        resultado = n1 + n2
        print(f"{n1:.2f} + {n2:.2f} = {resultado:.2f}")
        break
        

      
    elif opcao == 2:
        resultado = n1 * n2
        print(f"{n1:.2f} X {n2:.2f} = {resultado:.2f}")
        break
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f"O maior é o {maior:.2f}")
            break
        elif n1 < n2: 
            maior = n2
            print(f"O maior é o {maior:.2f}")
            break
        else:
            print("Os números são iguais")
            break
    
    elif opcao == 4:
        print(f"Novos números: {aleatorio1} e {aleatorio2}")
        break

    elif opcao == 5:
        break

    else:
        print("Opção inválida!")
        sleep(2)

        print('\033[35m-=-\033[m' * 20)
        print("""[1] Somar
[2] Multiplicar
[3] Verificar o maior
[4] Novos números 
[5] Sair do programa""")
        opcao = int(input('\033[36mO que você deseja fazer? \033[m' ))

print("Fim do programa")

    

