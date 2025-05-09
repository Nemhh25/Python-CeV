dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM percorridos? "))
valor_dias = 60 * dias
valor_km = 0.15 * km

print(f"{dias} dias alugados, {km}km rodados equivalem a um valor de R${valor_dias + valor_km:.2f}")