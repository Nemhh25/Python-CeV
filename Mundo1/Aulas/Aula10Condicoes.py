nome = input('Qual é o seu nome? ')

if nome == "Nelson":
    print("Que nome bonito!")

else:
    print("Seu nome é tão normal!")    

print(f"Bom dia, {nome}!")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

m = (n1 + n2) / 2
print(f"A média entre {n1} e {n2} é igual a {m:.1f}")

if m >= 6:
    print("Você está aprovado!")
else:
    print("Você está reprovado!")
