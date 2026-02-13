contador = 1
maior_Altura = 0
menor_Altura = 3.0
soma_alturas_h = 0
qtd_homens = 0
qtd_mulheres = 0

while contador <= 15:
    altura = float(input(f"Digite a altura da pessoa {contador}: "))
    genero = input(f"Digite o gênero da pessoa {contador} (h/m): ").lower()
    
    if altura > maior_Altura:
       maior_Altura = altura

    if altura < menor_Altura:
       menor_Altura = altura
    
    if genero == "h":
        soma_alturas_h += altura
        qtd_homens += 1
    elif genero == "m":
        qtd_mulheres += 1
    
    contador += 1
    
print(f"A maior altura é: {maior_Altura:.2f} m")
print(f"A menor altura é: {menor_Altura:.2f} m")
print(f"A quantidade de mulheres é: {qtd_mulheres}")
if qtd_homens > 0:
        media_altura_homens = soma_alturas_h / qtd_homens
        print(f"A média de altura dos homens é: {soma_alturas_h / qtd_homens:.2f}")
else:
        print("Não há homens para calcular a média de altura.")