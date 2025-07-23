class Autor():
    autores = []

    def __init__(self, nome, biografia):
        self.nome = nome
        self.biografia = biografia
        self.livros = []
        Autor.autores.append(self)

    def listar_obras(self):
        return [livro.titulo for livro in self.livros]
