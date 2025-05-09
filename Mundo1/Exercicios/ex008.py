medida = float(input("Digite uma distância em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f"A medida de {medida}m corresponde a:")
print(f"{km}km")
print(f"{hm}hm")
print(f"{dm}dm")
print(f"{dam}dam")
print(f"{cm}cm")
print(f"{mm}mm")