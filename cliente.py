import re

class Cliente:
    def __init__(self, nome, email, senha, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco

    def autenticar_email(self, email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$'
        return re.match(padrao, email) is not None

    def atualizar_cadastro(self):
        print("=====Atualização de Cadastro=====")
        novo_nome = input("Digite o novo nome: (ou enter para manter o atual) ")
        if novo_nome:
            self.nome = novo_nome

        novo_email = input("Digite o novo email: (ou enter para manter o atual) ")
        if novo_email:
            if Cliente.autenticar_email(novo_email):
                self.email = novo_email
            else:
                print("Email inválido. O email não foi atualizado.")

        nova_senha = input("Digite a nova senha: (ou enter para manter a atual) ")
        if nova_senha:
            self.senha = nova_senha

        novo_endereco = input("Digite o novo endereço: (ou enter para manter o atual) ")
        if novo_endereco:
            self.endereco = novo_endereco
            
        print("Cadastro atualizado com sucesso!")
