import datetime

data_atual = datetime.date.today()
ano_atual = data_atual.year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual} ")
if idade == 18:
   print("Você precisa se alistar imediatamente")

elif idade < 18:
   anos_faltantes = 18 - idade
   print(f"Ainda faltam {anos_faltantes} anos para você se alistar")

elif idade > 18:
   saldo = idade - 18
   print(f"Você já deveria se alistado em {saldo} anos")
    