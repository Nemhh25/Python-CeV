frase = "Curso em Vídeo Python"
print(frase[3:13]) # Pular de 2 em 2
print(frase[1:15]) # Pular de 2 em 2
print(frase[1:15:2]) # Pular de 2 em 2
print(frase[1::2]) # Pular de 2 em 2
print(frase[::2]) # Pular de 2 em 2
print(frase[::-1]) # Inverte a string
print(len(frase)) # Conta o número de caracteres
print(frase.count("o")) # Conta quantas vezes aparece o caractere "o"
print(frase.count("o", 0, 13)) # Conta quantas vezes aparece o caractere "o" entre os índices 0 e 13
print(frase.find("deo")) # Retorna a posição do primeiro caractere encontrado
print(frase.find("Android")) # Retorna -1 se não encontrar
print("Curso" in frase) # Verifica se Curso está na frase
print(frase.replace("Python", "Android")) # Troca Python por Android
print(frase.upper()) # Deixa tudo maiúsculo
print(frase.lower()) # Deixa tudo minúsculo
print(frase.capitalize())  # Deixa a primeira letra maiúscula e o restante minúscula
print(frase.title()) # Deixa a primeira letra maiúscula
print(frase.strip()) # Remove espaços no início e no final
print(frase.rstrip()) # Remove espaços no final
print(frase.lstrip()) # Remove espaços no início e no final
print(frase.split()) # Divide a string em uma lista
