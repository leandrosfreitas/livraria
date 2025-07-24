from autor import Autor
from livro import Livro
from carrinho_compra import CarrinhoCompra
from cliente import Cliente

machado = Autor("Machado de Assis", "Autor clássico do Brasil")
clarice = Autor("Clarice Lispector", "Autora modernista")

livro1 = Livro("12345", "Dom Casmurro", "Romance clássico", 39.9, "1899-01-01", 50, machado)
livro2 = Livro("67890", "A Hora da Estrela", "Obra marcante", 29.9, "1977-01-01", 30, clarice)
livro3 = Livro("44556", "Água Viva", "Narrativa introspectiva", 33.5, "1973-01-01", 15, clarice)
livro4 = Livro("54321", "Memórias Póstumas de Brás Cubas", "Romance inovador", 45.0, "1881-01-01", 40, machado)
livro5 = Livro("98765", "Quincas Borba", "Romance filosófico", 42.5, "1891-01-01", 20, machado)

def cadastrar_cliente():
    print("\n📝 Cadastro de novo cliente:")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    endereco = input("Endereço: ")
    return Cliente(nome, email, senha, endereco)

def main():
    carrinho = CarrinhoCompra()
    cliente = None

    while True:
        print("\n📚 Bem-vindo à Livraria!")
        print("1 - Fazer login")
        print("2 - Cadastrar novo cliente")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if cliente is None:
                print("⚠️ Nenhum cliente cadastrado. Faça o cadastro primeiro.")
                continue

            tentativas = 3
            while tentativas > 0:
                email = input("Email: ")
                senha = input("Senha: ")

                if cliente.email == email and cliente.senha == senha:
                    print(f"\n✅ Bem-vindo, {cliente.nome}!")
                    break
                else:
                    tentativas -= 1
                    print(f"❌ Email ou senha incorretos. Tentativas restantes: {tentativas}")

            if tentativas == 0:
                print("⚠️ Número de tentativas excedido. Voltando ao menu inicial.")
                continue

            while True:
                print("\n📚 Menu da Livraria:")
                print("1 - Listar obras por autor")
                print("2 - Exibir detalhes de um livro")
                print("3 - Comprar um livro")
                print("4 - Ver carrinho")
                print("5 - Atualizar cadastro")
                print("6 - Sair")

                opcao = input("\nEscolha uma opção: ")

                if opcao == "1":
                    for autor in Autor.autores:
                        print(f"\nObras de {autor.nome}:")
                        for titulo in autor.listar_obras():
                            print(f" - {titulo}")

                elif opcao == "2":
                    print("\nEscolha um livro para ver os detalhes:")
                    for i, livro in enumerate(Livro.livros, 1):
                        print(f'({i}) - {livro.titulo}')
                    escolha_livro = input("Digite o número do livro: ")

                    if escolha_livro.isdigit():
                        indice = int(escolha_livro) - 1
                        if 0 <= indice < len(Livro.livros):
                            detalhes = Livro.livros[indice].exibir_detalhes()
                            print("\n📖 Detalhes do livro:")
                            for chave, valor in detalhes.items():
                                print(f"{chave.capitalize()}: {valor}")
                        else:
                            print("Número inválido.")
                    else:
                        print("Entrada inválida.")

                elif opcao == "3":
                    print("\nEscolha um livro disponível no estoque:")
                    for i, livro in enumerate(Livro.livros, 1):
                        print(f'({i}) - {livro.titulo} (Estoque: {livro.estoque})')

                    escolha_livro = input("Qual livro deseja comprar? ")

                    if escolha_livro.isdigit():
                        indice = int(escolha_livro) - 1
                        if 0 <= indice < len(Livro.livros):
                            escolhido = Livro.livros[indice]
                            print(f"Você escolheu: {escolhido.titulo}")

                            try:
                                quantidade = int(input(f"Quantas unidades deseja de '{escolhido.titulo}'? "))
                                if quantidade <= 0:
                                    print("Quantidade inválida.")
                                elif quantidade > escolhido.estoque:
                                    print(f"Desculpe! Só temos {escolhido.estoque} unidade(s) em estoque.")
                                else:
                                    carrinho.adicionar(escolhido, quantidade)
                                    escolhido.estoque -= quantidade
                            except ValueError:
                                print("Por favor, digite um número válido.")
                        else:
                            print("Número inválido.")
                    else:
                        print("Entrada inválida.")

                elif opcao == "4":
                    if not carrinho.itens:
                        print("\n⚠️ Carrinho vazio.")
                    else:
                        while True:
                            print("\n🛒 Carrinho de Compras:")
                            for i, item in enumerate(carrinho.itens, 1):
                                print(f"({i}) - {item['quantidade']}x {item['livro'].titulo} - R$ {item['livro'].preco:.2f}")
                            print(f"\n💳 Total: R$ {carrinho.calcular_total():.2f}")

                            print("\nEscolha uma ação:")
                            print("1 - Remover um item")
                            print("2 - Finalizar compra")
                            print("3 - Voltar ao menu principal")
                            acao = input("Digite sua escolha: ")

                            if acao == "1":
                                indice = input("Digite o número do item que deseja remover: ")
                                if indice.isdigit():
                                    indice = int(indice) - 1
                                    if 0 <= indice < len(carrinho.itens):
                                        item_removido = carrinho.itens[indice]
                                        item_removido['livro'].estoque += item_removido['quantidade']
                                        carrinho.remover(item_removido['livro'])
                                        print(f"'{item_removido['livro'].titulo}' removido do carrinho.")
                                    else:
                                        print("Número inválido.")
                                else:
                                    print("Entrada inválida.")
                            elif acao == "2":
                                print("\n✅ Compra concluída com sucesso!")
                                print("Itens comprados:")
                                for item in carrinho.itens:
                                    print(f"- {item['quantidade']}x {item['livro'].titulo}")
                                print(f"\n💳 Total pago: R$ {carrinho.calcular_total():.2f}")
                                carrinho.itens.clear()
                                break
                            elif acao == "3":
                                print("↩️ Retornando ao menu principal...")
                                break
                            else:
                                print("Opção inválida.")

                elif opcao == "5":
                    cliente.atualizar_cadastro()

                elif opcao == "6":
                    print("Obrigado por visitar a livraria! 👋")
                    return

                else:
                    print("Opção inválida.")

        elif escolha == "2":
            cliente = cadastrar_cliente()
            print(f"\n✅ Cliente {cliente.nome} cadastrado com sucesso!")

        elif escolha == "3":
            print("Encerrando programa. Até logo!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
