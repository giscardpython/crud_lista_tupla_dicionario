import os

# Crie um CRUD utilizando os conceitos de lista, tupla e dicionário. 
# O usuário pode cadastrar quantas pessoas quiser. 
# Os dados a serem cadastrados são:
#- Nome
#- CPF
#- Telefone
#- E-mail
#- Profissão
#- Empresa

escolha = 1
opcao = 0
pessoas = []

while escolha > 0:
    print ("\nLista de Opções: \n")
    print('1 - Inserir pessoa')
    print('2 - Listar pessoas cadastradas')
    print('3 - Pesquisar pelo nome de uma pessoa')
    print('4 - Atualizar pessoa')
    print('5 - Deletar pessoa')
    print('6 - Sair do programa')

    opcao1 = int(input('\nEscolha a opção desejada (1 a 6):\n'))
    
    match opcao1:
        case 1:
            while True:
                nome = str(input("Informe o Nome da pessoa: "))
                if nome == '':
                    os.system('cls')
                    break
                cpf  = int(input('\nInforme o CPF: '))
                telefone = input('\nInforme o Telefone: ')
                email = input('\nInforme o E-mail: ')
                profissao = input('\nInforme a Profissão: ')
                empresa = input('\nInforme a Empresa: ')
                pessoa = {"Nome": nome, "CPF": cpf, "Telefone": telefone, "E-mail": email, "Profissão": profissao, "Empresa": empresa}
                pessoas.append(pessoa)
                print("Usuário criado com sucesso!\n")
        case 2:
            os.system('cls')
            print("Dados das Pessoas:\n")
            for i in range(len(pessoas)):
                print(f'\nÍndice: {i + 1}:')
                print(f'Nome: {pessoas[i]["Nome"]}')
                print(f'CPF: {pessoas[i]["CPF"]}')
                print(f'Telefone: {pessoas[i]["Telefone"]}')
                print(f'E-mail: {pessoas[i]["E-mail"]}')
                print(f'Profissão: {pessoas[i]["Profissão"]}')
                print(f'Empresa: {pessoas[i]["Empresa"]}')
        case 3:
            # usuário informa o nome que deseja procurar
            nome = input('Informe o nome que deseja encontrar: ').capitalize()
            for i in range(len(pessoas)):
                if nome in pessoas[i]['Nome']:
                    print(f'\nÍndice: {i + 1}')
                    print(f'Nome: {pessoas[i]["Nome"]}')
                    print(f'CPF: {pessoas[i]["CPF"]}')
                    print(f'Telefone: {pessoas[i]["Telefone"]}')
                    print(f'E-mail: {pessoas[i]["E-mail"]}')
                    print(f'Profissão: {pessoas[i]["Profissão"]}')
                    print(f'Empresa: {pessoas[i]["Empresa"]}')
                else:
                    print(f'{nome} não encontrado na lista.')
                    continue
        case 4:
            indice = int(input('Informe o índice a ser alterado: '))
            campo = input('Informe o nome do campo a ser alterado: ')
            indice -= 1
            try:
                pessoas[indice][campo] = input(f'Informe o novo valor do campo {campo}: ')
            except:
                print('Não foi possível alterar.')
            # novos dados são exibidos na lista
            print(f'Novos dados do índice {indice + 1}:\n')
            print(f'Nome: {pessoas[indice]["Nome"]}')
            print(f'CPF: {pessoas[indice]["CPF"]}')
            print(f'Telefone: {pessoas[indice]["Telefone"]}')
            print(f'E-mail: {pessoas[indice]["E-mail"]}')
            print(f'Profissão: {pessoas[indice]["Profissão"]}')
            print(f'Empresa: {pessoas[indice]["Empresa"]}')
        case 5:
            # usuário informa o índice a ser excluído
            indice = int(input('Informe o índice que deseja deletar da lista de dicionários: \n'))
            indice -= 1
            try:
                del[pessoas[indice]]
            except:
                print('Não foi possível deletar o índice.')
            # nova lista é exibida
            for i in range(len(pessoas)):
                print(f'\nÍndice: {i + 1}:')
                print(f'Nome: {pessoas[i]["Nome"]}')
                print(f'CPF: {pessoas[i]["CPF"]}')
                print(f'Telefone: {pessoas[i]["Telefone"]}')
                print(f'E-mail: {pessoas[i]["E-mail"]}')
                print(f'Profissão: {pessoas[i]["Profissão"]}')
                print(f'Empresa: {pessoas[i]["Empresa"]}')
        case 6:
            escolha = 0
            break
        case _:
            print('Opção inváida! Digite uma opção de 1 a 6')
            continue 