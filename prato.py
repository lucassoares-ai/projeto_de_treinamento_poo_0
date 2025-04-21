class Prato:
    def __init__(self, nome, preco):

        assert type(nome) == str, "O nome do prato deve estar no formato str"
        assert type(preco) == float, "O preço do prato deve ser descrito utilizando no formato float"

        self._nome = nome 
        self._preco = preco 


    @property 
    def nome(self):
        return self._nome 


    @property
    def preco(self):
        return self._preco 




