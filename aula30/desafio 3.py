print('TAMANHO DO NOME')
nome = str(input('Nome: ')).strip().capitalize()
if len(nome) <= 4:
    print(f'Olá, {nome}. Seu nome é curto!')
elif len(nome) <= 6:
    print(f'Olá, {nome}. Seu nome é normal!')
else:
    print(f'Olá, {nome}. Seu nome é muito grande!')
