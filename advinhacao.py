print("***************************")
print("Bem vindo ao Jogo de Advinhação")
print("***************************")

numero_secreto = 42

chute_str = input("Digite o seu número:")

print("você digitou " , chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou")
else:
    if(chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    if (chute < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")

print("fim do jogo")