km = float(input('Qual sua velocidade em km/h? '))
if km > 80:
    print('\033[1;31mVocê foi multado!\033[m')
    multa = (km - 80) * 7
    print(f'\033[1;37mO valor da multa é de R${multa:.2f}.\033[m')
else:
    print('\033[1;32mVocê está dentro do limite de velocidade.\033[m')
    