from autor import Autor

class Livro():
    livros = []
    def __init__(self, isbn, titulo, descricao, preco, data_publicacao, estoque, autor: Autor):
        self.isbn = isbn
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.data_publicacao = data_publicacao
        self.estoque = estoque
        self.autor = autor
        
        autor.livros.append(self)
        Livro.livros.append(self)

        livro_dict = {
            'isbn': self.isbn,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'preco': self.preco,
            'data_publicacao': self.data_publicacao,
            'estoque': self.estoque,
            'autor': self.autor.nome
        }

        

    def exibir_detalhes(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "preco": self.preco,
            "data_publicacao": self.data_publicacao,
            "estoque": self.estoque,
            "autor": self.autor.nome
        }
