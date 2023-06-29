print("Bem vindo ao jogo de advinhação!")

numero_magico = 42

total_de_tentatives = 3
rodada = 1

while (rodada <= total_de_tentatives):
    print("Tentativa {} de {}".format(rodada,total_de_tentatives))

    chute = int(input("Tente advinhar o número magico: "))

    if(chute == numero_magico):
        print("Acertou!")

    elif(chute > numero_magico):
        print("Errou, Chutou alto!")
    else:
        print("Errou, chutou baixo!")

    rodada = rodada + 1