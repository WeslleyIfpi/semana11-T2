def cadastro():
    qtdPessoas = 0
    somatorio = 0
    menorIdade = 200
    maiorIdade = 0
    mediaIdade = 0

    while True:
        idade = int(input())
        if idade == 0 : break
        else:
            qtdPessoas += 1
            somatorio += idade
            if idade < menorIdade:
                menorIdade = idade
            elif idade > maiorIdade:
                maiorIdade = idade
    if qtdPessoas > 0:
        mediaIdade = somatorio / qtdPessoas 

    return qtdPessoas, mediaIdade, menorIdade, maiorIdade





def main():
    qtdPessoas, idadeMedia, menorIdade, maiorIdade = cadastro()
    if idadeMedia > 0:
        print(qtdPessoas)
        print(idadeMedia)
        print(menorIdade)
        print(maiorIdade)


if __name__ == "__main__":
    main()