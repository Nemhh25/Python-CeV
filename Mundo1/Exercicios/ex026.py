frase = input('Digite uma frase: ').strip().upper()
print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"Ela aparece na primeira vez na posição {frase.find('A')+1}")
print(f"Ela aparece pela última vez na posição {frase.rfind('A')+1}")