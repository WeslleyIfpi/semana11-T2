def menu():
    while True:
        escolha = int(input('OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM\n'))

        if escolha == 0:
            print('0 - Fim de serviço.')
            break
        elif escolha == 1:
            print('1 - Olá. Como vai?')
        elif escolha == 2:
            print('2 - Vamos estudar mais.')
        elif escolha == 3:
            print('3 - Meus Parabéns!')
        else:
            print('Opção inválida.')


def main():
    menu()

if __name__ == '__main__':
    main()