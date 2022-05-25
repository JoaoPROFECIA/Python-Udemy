print('PAR OU ÍMPAR')
while True:
    num_inteiro = input('Digite um número: ')
    if num_inteiro.isdigit():
        num_inteiro = int(num_inteiro)
        if num_inteiro % 2 == 0:
            print(f'O número {num_inteiro} é par')
        else:
            print(f'O número {num_inteiro} é ímpar')
    else:
        print('Isso não é um número inteiro. Tente novamente.')