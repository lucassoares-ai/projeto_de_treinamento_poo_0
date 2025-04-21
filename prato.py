import time 

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


    # Agora eu vou utilizar os setters para que eu posso alterar os atributos publicamente. 
    # No caso eu estou fazendo isto apenas para treinamento. 

    @nome.setter 
    def nome(self, novo_nome):
        self._nome = novo_nome 


    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco 


    # Criando um método que nos permite alterar as informações daquele prato 


    def alterar_info(self):
        # quantidade_info = int(input("Inidique a quantidade de informações que você gosteria acerca deste prato"))

        def alterando_info():
            print("...")
            time.sleep(2)
            print(f"Para alterar o nome do prato {self._nome} digite 1.")
            print(f"Para alterar o preco do prato {self._nome} digite 2.")
            print("Para sair digite 4.")

            opcao = int(input("Indique a sua opção: "))

            if opcao == 1:
                print(f"Alterando o nome do prato {self._nome}")
                time.sleep(2)
                novo_nome = input(f"Indique o novo nome do prato {self._nome}: ")

                self._nome = novo_nome 
                print("Nome alterado!")
                time.sleep(2)

                alterando_info()

            elif opcao == 2:
                print(f"Alterando o preço do prato {self._nome}.")
                print("...")
                time.sleep(2)
                novo_preco = float(input(f"indique o novo preço do prato {self._nome}: "))

                self._preco = novo_preco

                print("Preço alterado!")
                time.sleep(2)

                alterando_info()

            elif opcao == 4:

                print("Encerrando operação...")
                time.sleep(2)

            else:

                print("Opção invalida.")
                time.sleep(2)

                print("Tentando novamente...")
                time.sleep(2)

                alterando_info()

        try: 
            alterando_info()

        except  ValueError as a:
            print(a)
            print("A sua opção deve ser indicada utilizando um tipo de dado numérico.")
            print("O novo preço do prato também deve ser indicado utilizando um tipo de dado numérico.")

            alterando_info()



# prato = Prato("Pizza", 10.99)

# prato.alterar_info()

# print(prato.nome)

# prato.nome = "pizza"

# print(prato.nome)




