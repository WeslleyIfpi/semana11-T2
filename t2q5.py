def conceito():
    while True:
        nota = float(input())
        if  nota < 0 or nota > 10:
            print('Nota inválida.')
        else:
            if nota >= 8.5:
                return 'A'
            elif nota >= 7.0:
                return 'B'
            elif nota >= 5.0:
                return 'C'
            elif nota >= 4.0:
                return 'D'
            else:
                return 'E'

def main():
    print(conceito())

if __name__ == '__main__':
    main()