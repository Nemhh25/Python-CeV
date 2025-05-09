import math
ca = float(input("Digite o comprimento do cateto adjacente: "))
co = float(input("Digite o comprimento do cateto oposto: "))
hip = math.hypot(ca, co)
print(f"A hipotenusa vai medir {hip:.2f}")