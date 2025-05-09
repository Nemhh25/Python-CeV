# Ordem de precedência dos operadores aritméticos
# 1. ()
# 2. ** (exponenciação)
# 3. * (multiplicação) e / (divisão) e // (divisão inteira) e % (módulo)
# 4. + (adição) e - (subtração)
# > alinhamento à direita
# < alinhamento à esquerda
# ^ alinhamento ao centro

n1 = int(input('Digite um número: '))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
modulo = n1 % n2

print(f"A soma vale {n1 + n2}")
print(f"A subtração vale {subtracao}")
print(f"A multiplicação vale {multiplicacao}")
print(f"A divisão vale {divisao:.2f}")  # Formatação para duas casas decimais
print(f"A divisão inteira vale {divisao_inteira}")
print(f"A exponenciação vale {exponenciacao}")
print(f"O módulo vale {modulo}")