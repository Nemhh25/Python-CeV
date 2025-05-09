num = int(input("\033[1;33mDigite um número:\033[m "))

if num % 2 == 0:
    print(f"\033[1;36mO número {num} é um número par. \033[m ")

else:
    print(f"\033[1;37mO número {num} é um número impar. \033[m ")
    