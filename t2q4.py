def cardapio():
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')


def calcula():
    total = 0
    while True:
        cardapio()
        codigo = input().upper().strip()
        if codigo == 'H':
            total += 5.50 
        elif codigo == 'C':
            total += 6.80 
        elif codigo == 'M':
            total += 4.50 
        elif codigo == 'A':
            total += 7.00 
        elif codigo == 'Q':
            total += 4.00
        elif codigo == 'X':
            break
    return total

def main():
    print(f'{calcula():.2f}')

if __name__ == '__main__':
    main()