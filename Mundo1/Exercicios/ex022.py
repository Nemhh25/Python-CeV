nome = input("Digite seu nome: ").strip()
primeiro_nome = nome.split()[0]
print(f"Seu nome em maiúsculas é: {nome.upper()}")
print(f"Seu nome em minúsculas é: {nome.lower()}")
print(f"Seu nome tem: {len(nome) - nome.count(' ')} letras")

print(f"Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras")
