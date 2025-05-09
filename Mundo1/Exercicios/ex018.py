import math

angulo = float(input("Digite o ângulo: "))

angulo_convertido = math.radians(angulo)

seno = math.sin(angulo_convertido)
cosseno = math.cos(angulo_convertido)
tangente = math.tan(angulo_convertido)

print(f"O seno de {angulo} é {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}")