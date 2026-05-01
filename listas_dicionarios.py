import os

alunos = ['João', 'Pedro', 'Ana', 'Victor', 'Kaio']
nome = str(input('Digite o seu nome: '))

cadastro = {
    'João': 20,
    'Pedro': 25,
    'Ana': 19,
    'Victor': 22,
    'Kaio': 21
}

def verificar_cadastro():
    if nome in alunos:
        idade = int(input(f'Olá {nome}, para confirmar a sua identidade, digite sua idade: '))
        if cadastro.get(nome) == idade:
            print(f'Bem-vindo, {nome}!')
        else:
            print('Idade incorreta, acesso negado.')
    else:
        criando_cadastro()

def criando_cadastro():
    print('Seu nome não está cadastrado, acesso negado.')
    tentativa = int(input('Deseja cadastrar seu nome? Digite 1 para sim, 2 para não ou 3 para reiniciar: '))
    if tentativa == 1:
        nome_aluno = str(input('Digite seu nome: '))
        idade_aluno = int(input('Digite sua idade: '))
        cadastro[nome_aluno] = idade_aluno
        alunos.append(nome_aluno)
        print(f'Cadastro finalizado, seja bem-vindo, {nome_aluno}')
    elif tentativa == 2:
        os.system('python3 listas_dicionarios.py')
    else:
        print('Ok, sistema sendo reiniciado...')
        os.system('python3 listas_dicionarios.py')

verificar_cadastro()

