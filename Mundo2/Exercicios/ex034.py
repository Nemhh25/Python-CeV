salario = float(input("Digite seu salário: R$"))
aumento = 0.0

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print(f"Seu salário de R${salario:.2f} aumentou para R${aumento:.2f} ")

else:
    aumento = salario + (salario * 0.15)
    print(f"Seu salário de R${salario:.2f} aumentou para R${aumento:.2f}")
