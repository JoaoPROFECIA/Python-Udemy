"""
Validador de CPF
"""
from time import sleep
def validador_de_cpf(cpf):
    while True:
        cpf = input('Digite um CPF: ')
        novo_cpf = cpf[:9]
        reverso = 10
        total = 0

        for index in range(19):
            if index > 8:
                index -= 9
            
            total += int(novo_cpf[index]) * reverso

            reverso -= 1
            if reverso < 2:
                reverso = 11
                diferenca = 11 - (total % 11)

                if diferenca > 9:
                    diferenca = 0
                total = 0
                novo_cpf += str(diferenca)

        if novo_cpf == cpf: 
            print('CPF VÁLIDO')
            sleep(1)
        else:
            print('CPF INVÁLIDO')
            sleep(1)

validador_de_cpf(cpf='')