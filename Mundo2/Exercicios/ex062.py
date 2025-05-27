primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro_termo
n = 1   
total = 0
mais = 10

while mais != 0:    
    total = total + mais
    while n <= total:
        print(f"{termo}", end=" ")
        termo += razao
        n+=1

    print(" -> PAUSA")
    mais = int(input("Quantos termos você quer mostrar mais? "))




        

  