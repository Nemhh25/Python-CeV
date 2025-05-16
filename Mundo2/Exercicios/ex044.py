preco_compras = float(input("Digite o preço das compras: "))
condicoes = int(input("""Digite a forma de pagamento: 
[1] Dinheiro/Cheque a vista
[2] Cartão a vista
[3] 2x no cartão
[4] 3x ou mais no cartão 
 """))

if condicoes == 1: 
    print(f"Ao escolher essa forma de pagamento, sua compra no valor de R${preco_compras:.2f} sai com desconto de 10%. Você precisa pagar R${preco_compras - (preco_compras * 0.1)} ")

elif condicoes == 2:
    print(f"Ao escolher essa forma de pagamento, sua compra no valor de R${preco_compras:.2f} sai com desconto de 5%. Você precisa pagar R${preco_compras - (preco_compras * 0.05)} ")

elif condicoes == 3:
    print(f"Ao escolher essa forma de pagamento, sua compra no valor de R${preco_compras:.2f} sai pelo preço normal.")

elif condicoes == 4:
    parcelas = int(input("Quantas vezes? "))
    juros = preco_compras * 0.2
    print(f"Ao escolher essa forma de pagamento, sua compra no valor de R${preco_compras:.2f} sai com 20% de juros. Totalizando {parcelas}x de {(preco_compras + juros) / parcelas}. Valor total: R${preco_compras + juros}")    

else:
    print("Opção inválida.")