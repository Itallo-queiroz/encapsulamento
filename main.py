import classe as cl

if __name__ == '__main__':
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe o E-mail: ')

    # instancia da classe
    usuario = cl.Pessoa(nome, idade, email)

    # saida de dados
    print(f'\nNome: {usuario.nome}. ')
    print(f'\nIdade: {usuario.idade}. ')
    print(f'\nE-mail: {usuario.email}. \n')