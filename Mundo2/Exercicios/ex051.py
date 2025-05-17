primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
n = int(input("Quantos elementos exibir: "))

ultimo = primeiro_termo + (n-1)*razao
ultimo = ultimo + 1

for var in range(primeiro_termo, ultimo, razao):
    print(var)