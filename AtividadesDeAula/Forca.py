import random
def jogar():


    mensagemDeAbertura()

    palavra_secreta = geraPalavraSecreta()

    configuraLetrasAcertadas(palavra_secreta)



    acertou = False
    enforcou = False
    erros = 0

    while(not acertou and not enforcou):
        chute = pedirChute()
        if(chute in palavra_secreta):
            posicao = 0

            for letra in palavra_secreta:
                if(chute == letra.upper()):
                    letras_acertadas[posicao] = letra
                posicao += 1

        else:
            erros += 1
        print(letras_acertadas)

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

    if(acertou):
        print('Voce ganhou')
    else:
        print('Voce foi enforcado')



def mensagemDeAbertura():
    print("Bem vindo ao jogo da forca")

def geraPalavraSecreta():
    arquivo = open("palavras1.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def configuraLetrasAcertadas(palavra):
    letras_acertadas = ['_' for letra in palavra]

def pedirChute():
    chute = input('Qual letra?\n').upper()
    return chute