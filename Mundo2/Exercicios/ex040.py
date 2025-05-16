n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5.0:

    print(f"Com {media:.2f} de nota você foi REPROVADO ")

elif media >= 7:
    print(f"Com {media} de nota você foi APROVADO")

else:
    print(f"Com {media} de nota você ficou de RECUPERAÇÃO")        