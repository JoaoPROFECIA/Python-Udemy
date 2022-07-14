"""
Funções em Python - return
"""

'''def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return "Não é possível dividir por zero!"

divide = divisao(10, 0)
print(divide)'''

"""
Exercicios propostos
"""


"""
1 - Criar uma função que exiba o nome do usuário e a mensagem "Olá, [nome]!"
"""
def saldacao(nome):
    nome = str(input("Digite seu nome: "))
    return "Olá, " + nome

saldar = saldacao(nome='')
print(saldar)


"""
2 - Criar uma função que receba 3 números como parâmentros e retorne a soma 
dos mesmos
"""
def soma(n1, n2, n3):
    return n1 + n2 + n3

soma = soma(1, 2, 3)
print(soma)


"""
3 - Criar uma função que receba 2 números. O primeiro é um valor e o segundo 
é o percentual (ex: 10%).
Retorne (return) o valor do primeiro número somado ao aumento do percetual 
do mesmo
"""
def percentual(n1, n2):
    return n1 * n2 / 100

porcentagem = percentual(10, 5)
print(porcentagem)


"""
4 - Fizz Buzz - Se o parâmetro for divisível por 3, retorne Fizz, se for 
divisível por 5, 
retorne Buzz, se for divisível por 3 e 5, retorne FizzBuzz.
"""
def fizzbuzz(n1):
    n1 = int(input("Digite um número: "))
    if n1 % 3 == 0 and n1 % 5 == 0:
        return "FizzBuzz"
    elif n1 % 3 == 0:
        return "Fizz"
    elif n1 % 5 == 0:
        return "Buzz"
    else:
        return n1
    
fizzbuzz = fizzbuzz(15)
print(fizzbuzz)
