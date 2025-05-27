primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo
n = 1   



while n <= 10:
    print(f"{termo}", end=" ")
    termo += razao
    n+=1
  