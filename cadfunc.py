import random

#--- inicio das variaveis globais ---
lista_funcionario = []
id_funcionario = 0
#--- fim das variaveis globais ---

#--- Inicio do cadastro
def cadastrar_funcionario(id): 
    print('Bem vindo ao menu de cadastro')
    id = random.randint(1, 1000)
    print('Id do funcionario: 00{}'.format(id))
    nome = input('Entre com o NOME do funcionario: ')
    setor = input('Entre com o SETOR do funcionario: ')
    salario = float(input('Entre com o SALARIO do funcionario: '))
    dicionario_funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    lista_funcionario.append(dicionario_funcionario.copy())                          
#--- fim do cadastro

#--- Inicio da pesquisa 
def consultar_funcionario(): 
    while True:
        print('Bem vindo ao menu de consulta')
        opcao_consultar = input('\nEscolha a opcao desejada: \n' +
                                '1 - Consultar todos os funcionarios\n'+
                                '2 - Consultar funcionario por ID\n'+
                                '3 - Consultar funcionario por setor\n'+
                                '4 - Retornar\n '+
                                '>>> ')

        if opcao_consultar == '1':
            print('Voce escolheu a opcao consultar todos os funcionarios')
            for funcionario in lista_funcionario:
                print('---------------------------')
                for key, value in funcionario.items():
                    print('{} : {}'.format(key, value))
                print('---------------------------')

        elif opcao_consultar == '2':
            print('Voce escolheu a opcao consultar funcionario por ID') 
            id_desejado = int(input('Entre com o ID desejado: '))
            encontrado = False
            for funcionario in lista_funcionario:
                if funcionario['id'] == id_desejado:
                    print('---------------------------')
                    for key, value in funcionario.items():
                        print('{} : {}'.format(key, value))
                    print('---------------------------')
                    encontrado = True
                    break  # Não é necessário continuar procurando
            if not encontrado:
                print('Funcionario com ID {} nao encontrado.'.format(id_desejado))

        elif opcao_consultar == '3':
            print('Voce escolheu a opcao consultar funcionario por setor')
            setor_desejado = input('Entre com o setor desejado: ')
            for funcionario in lista_funcionario:
                if funcionario['setor'] == setor_desejado:
                    print('---------------------------')
                    for key, value in funcionario.items():
                        print('{} : {}'.format(key, value))
                    print('---------------------------')

        elif opcao_consultar == '4':
            return  # sai da funcao e volta para o main
        else:
            print('Opcao invalida. Tente novamente') 
            continue   # volta para o inicio do laco
#--- fim da pesquisa 

#--- inicio do remover
def remover_funcionario(): 
    print('Bem vindo ao menu de remover')
    id_desejado = int(input('Entre com o ID do funcionario que deseja remover: '))
    for funcionario in lista_funcionario:
        if funcionario['id'] == id_desejado:
            lista_funcionario.remove(funcionario)
            print('Funcionario removido!')
            return  # Encerra a função após remover
    print('Funcionario com ID {} nao encontrado.'.format(id_desejado))
#--- fim do remover

#--- Inicio do main
print('Bem vindo ao sistema de controle de funcionarios')
while True:
    opcao_principal = input('\nEscolha a opcao desejada: \n' +
                            '1 - Cadastrar funcionario\n'+
                            '2 - Consultar funcionario\n'+
                            '3 - Remover funcionario\n'+
                            '4 - Sair\n '+
                            '>>> ')
    if opcao_principal == '1':
        id_funcionario += 1
        cadastrar_funcionario(id)
    elif opcao_principal == '2':
        consultar_funcionario()  
    elif opcao_principal == '3':
        remover_funcionario()
    elif opcao_principal == '4':
        break  # encerra o laco principal
    else:
        print('Opcao invalida. Tente novamente') 
        continue   # volta para o inicio do laco
#--- Fim do main
