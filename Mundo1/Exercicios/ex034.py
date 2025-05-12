valor = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salário: R$"))
ano = int(input("Quantos anos de financiamento? "))
prestacao = valor / (ano * 12)
limite = salario * 0.3

print(f'Para pagar uma casa de R${valor} em {ano} anos, a prestação será de {prestacao:.2f}')
if prestacao >= limite:
    print("Empréstimo negado")

else: 
    print("Empréstimo concedido")