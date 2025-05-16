from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"{idade} anos")
    print("Classificação: MIRIM")

elif idade >= 10 and idade <= 14:
    print(f"{idade} anos")
    print("Classificação: INFANTIL")

elif idade > 14 and idade <= 19:
    print(f"{idade} anos")
    print("Classificação: JUNIOR")

elif idade > 19 and idade <= 25:
    print(f"{idade} anos")
    print("Classificação: SÊNIOR")

else:
    print(f"{idade} anos")
    print("Classificação: MASTER")    


