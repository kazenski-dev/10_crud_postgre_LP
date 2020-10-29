from operation import Manipulacao
from conexao import Conexao
from service import *
from cadastro import Pessoa

def mostra_menu ():
    print(30 * "-")
    print("1- Inserir cadastro")
    print("2- Buscar por nome")
    print("3- Buscar por email")
    print("4- Buscar por cpf")
    print("5- Verificar se cadastro ativo")
    print("6- Verificar se cadastro inativo")
    print("Digite numero ZERO para sair")
    print(30 * "-")

def executa_menu():
    while True:
        mostra_menu()
        opcao = int(input("Insira a opcao que deseja: "))
        if opcao == 1:
            print("1- Inserir cadastro selecionado")
            Pessoa.cadastro()

        elif opcao == 2:
            print("2- Buscar por nome selecionado")
            nome_inserido = input("Insira o nome: ")
            Manipulacao.busca_nome(nome_inserido)

        elif opcao == 3:
            print("3- Buscar por email selecionado")
            email_inserido = input("Insira o email: ")
            Manipulacao.busca_email(email_inserido)

        elif opcao == 4:
            print("4- Buscar por cpf selecionado")
            cpf_inserido = input("Insira o cpf: ")
            Manipulacao.busca_cpf(cpf_inserido)

        elif opcao == 5:
            print("5- Verificar se cadastro ativo")
            cpf_inserido = input("Insira o cpf: ")
            Manipulacao.busca_pessoa_cpf(cpf_inserido)

        elif opcao == 6:
            print("6- Verificar se cadastro inativo")
            Manipulacao.busca()

        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Valor invalido, digite novamente")
            continue