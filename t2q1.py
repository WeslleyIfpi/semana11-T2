def somaNumeros():
    somatorio = 0
    while True:
        entrada = int(input())
        if entrada == 0: break
        else:
            somatorio += entrada
    return somatorio

def main():
    total = somaNumeros()
    print(f'{total}')


if __name__ == '__main__':
    main()