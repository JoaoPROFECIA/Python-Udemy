"""
Gerador de CPF
"""

from random import randint

numero = str(randint(100000000, 999999999))

novo_cpf = numero                   
reverso = 10                                 # Contador reverso
total = 0                             

# Loop do CPF
for index in range(19):
    if index > 8:                            # Primeiro índice vai de 0 a 9
        index -= 9                           # São os 9 primeiros dígitos do CPF

    total += int(novo_cpf[index]) * reverso  # SValor total da multiplicação
    
    reverso -= 1                             # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        diferenca = 11 - (total % 11)

        if diferenca > 9:                    # Se o dígito for maior que 9 o valor é 0
            diferenca = 0
        total = 0                            # Zera o total
        novo_cpf += str(diferenca)           # Adiciona o dígito ao CPF

print(f'O novo CPF gerado é: {novo_cpf}')