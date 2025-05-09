import datetime

ano = int(input("Digite o ano que quer analisar: 0 para ano atual: "))
data_atual = datetime.date.today()
ano_atual = data_atual.year

if ano == 0:
    ano = ano_atual
    
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

        print(f"{ano}. Esse ano é bissexto")
else:
        print(f"{ano}. Esse ano não é bissexto")