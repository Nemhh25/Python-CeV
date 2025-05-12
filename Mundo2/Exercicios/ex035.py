print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)
primeiro_segmento = float(input("Digite o primeiro segmento:"))
segundo_segmento = float(input("Digite o segundo segmento:"))
terceiro_segmento = float(input("Digite o terceiro segmento:"))

if (primeiro_segmento + segundo_segmento > terceiro_segmento and
    primeiro_segmento + terceiro_segmento > segundo_segmento and
    segundo_segmento + terceiro_segmento > primeiro_segmento):
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima NÃO podem formar um triângulo!")