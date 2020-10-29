from operation import Manipulacao
from service import *

class Pessoa():
    def cadastro(self):
        bd = Manipulacao()
       
        self.cpf = False
        #Looping de solicitação e validação de CPF
        while cpf == False:
            c_cpf = list(input('CPF: '))
            c_cpf = ''.join(c_cpf)
            validador_cpf = ValidadorCPF(c_cpf)
            if validador_cpf.validador():
                c_cpf = validador_cpf._snumeros(c_cpf)
                existe = bd.busca_cpf(c_cpf)
                if existe:
                    print("CPF já cadastrado")
                    cpf = False
                else:
                    cpf = True
            else:
                print("CPF inválido!")
                cpf = False
               
        self.nome = False
        #Looping de solicitação e validação de nome
        while nome == False:
            c_nome = list(input("Nome: "))
            c_nome = ''.join(c_nome).upper()
            validador_nome = ValidadorNome()
            if validador_nome.validador(c_nome):
                nome = True
            else:
                print("Nome inválido")
                nome = False

        self.email = False
        #Looping de solicitação e validação de e-mail
        while email == False:
            c_email = list(input("E-mail: "))
            c_email = ''.join(c_email).upper()
            validador_email = ValidadorEmail()
            if validador_email.validador(c_email):
                email = True
            else:
                print("E-mail inválido")
                email = False

        #inserir dados no banco
        return bd.inserir(c_cpf,c_nome,c_email)
