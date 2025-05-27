n = int(input("Quantos termos você quer mostrar? "))

primeiro = 0
segundo = 1
print(f"{primeiro} > {segundo}")


contador = 3
while contador <= n:
    terceiro = primeiro + segundo
    print(f"{terceiro}", end= ", " if contador < n else ".")
    primeiro = segundo
    segundo = terceiro
    contador += 1
