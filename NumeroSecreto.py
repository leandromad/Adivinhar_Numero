#Este é um jogo de adivinhar o número
import random
NumeroSecreto = random.randint(1,20)
print("Estou pensando em um número entre 1 e 20")

#Peça para o usuário adivinhar o número em 6 tentativas
for Tentativas in range(1,7):
    chute = int(input("Qual é o seu chute? "))
    if chute < NumeroSecreto:
        print("Seu chute é baixo")
    elif chute > NumeroSecreto:
        print("Seu chute é alto")
    else:
        break

if chute == NumeroSecreto:
    print("Muito bem! Você adivinhou o número em " + str(Tentativas) + " tentativas")
else:
    print("Você não conseguiu adivinhar o número. O número é " + str(NumeroSecreto))