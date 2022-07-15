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
def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'João')	
saudacao('Oi', 'Maria')
saudacao('Hey', 'Eduardo')



"""
2 - Criar uma função que receba 3 números como parâmentros e retorne a soma 
dos mesmos
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(1, 2, 3)


"""
3 - Criar uma função que receba 2 números. O primeiro é um valor e o segundo 
é o percentual (ex: 10%).
Retorne (return) o valor do primeiro número somado ao aumento do percetual 
do mesmo
"""
def aumento_percentual(n1, n2):
    return n1 + (n1 * n2 / 100)

ap = aumento_percentual(50, 10)
print(ap)


"""
4 - Fizz Buzz - Se o parâmetro for divisível por 3, retorne Fizz, se for 
divisível por 5, 
retorne Buzz, se for divisível por 3 e 5, retorne FizzBuzz.
"""
def fizzbuzz(n):
    if n==0:
        return ZeroDivisionError (f"{n} Não é possível dividir por zero!")
    if n % 3 == 0 and n % 5 == 0:
        return f"FizzBuzz, {n} é divisivel por 3 e 5"
    if n % 3 == 0:
        return f"Fizz, {n} é divisivel por 3"
    if n % 5 == 0:
        return f"Buzz, {n} é divisivel por 5"
    
    return n

from random import randint
for i in range(100):
    n = randint(0, 100)
    print(fizzbuzz(n))
