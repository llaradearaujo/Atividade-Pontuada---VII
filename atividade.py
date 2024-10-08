import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def IMC(peso, altura):
    imc = peso / (altura*altura)
    return imc

def resultado(imc):
    if imc < 18.5:
        resultado = "abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        resultado = "peso normal"
    elif imc >=25 and imc < 30:
        resultado = "sobrepeso"
    elif imc >= 30 and imc < 35:
        resultado = "obesidade grau 1"
    elif imc >= 35 and imc < 40:
        resultado = "obesidade grau 2"
    else:
        resultado = "obesidade grau 3(mórbida)"
    return resultado

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []
imcs = []
resultados = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    sobrenome = input("digite seu sobrenome: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    imc = IMC(peso, altura)
    resultado_imc = resultado(imc)
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    imcs.append(imc)
    resultados.append(resultado_imc)


# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"\nUsuário {i+1}:")
    print("Nome:", nomes[i])
    print("Sobrenome:", sobrenomes[i])
    print("Nome completo:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC:", round(imcs[i],2))
    print("resultado:", resultados[i] )
