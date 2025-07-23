class CarrinhoCompra:
    def __init__(self, itens=None):
        self.itens = itens if itens is not None else []

    def adicionar(self, livro, quantidade):
        self.itens.append({
            'livro': livro,
            'quantidade': quantidade
        })
        print(f"{quantidade} unidade(s) de '{livro.titulo}' adicionada(s) ao carrinho.")

    def remover(self, livro):
        self.itens = [item for item in self.itens if item['livro'] != livro]
        print(f"'{livro.titulo}' removido do carrinho.")

    def calcular_total(self):
        return sum(item['livro'].preco * item['quantidade'] for item in self.itens)

