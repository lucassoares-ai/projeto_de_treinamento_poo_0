from pedido import Pedido
# from prato import Prato
import funcoes
import time
class Restaurante:

    def __init__(self, nome= None, telefone= None, endereco= None, uvp= None):

        if nome:
            assert type(nome) == str, "O nome deve estar no tipo de dados str"

        if telefone:
            assert type(telefone) == str, "O número de telefone deve estar no tipo de dados str."

        if endereco:
            assert type(endereco) == str, "O endereço deve estar descrito utilizando o tipo de dados str."

        if uvp:
            assert type(uvp) == str, "O endereço deve estar descrito utilizando o tipo de dados str"

        self._nome = nome 
        self._telefone = telefone 
        self._endereco = endereco
        self._uvp = uvp

        self._caixa = 0  
        self._pedidos = []
        self._cardapio = []


    def mostrar_info(self):
        print(f"""
        Nome: {self._nome}
        Esloga: {self._uvp}
        Telefone: {self._telefone}
        Endereço: {self._endereco}""")


    def alterar_info(self):

        while True:

            print("Alterando funções...")
            time.sleep(2)

            print("Digite 1 para alterar o nome do restaurante.")
            print("Digite 2 para alterar a frase de proposição de valor do restaurante.")
            print("Digite 3 para alterar o número de telefone do restaurante.")
            print("Digite 4 para alterar o endereço do restaurante.")
            print("Para encerrar o sistema digite 5.")

            opcao = int(input("Indique a sua opção: "))

            if opcao == 1:

                def alterar_nome():
                    novo_nome = input("Indique o novo nome do restaurante: ")
                    print("Alterando nome...")
                    time.sleep(2)
                    if len(novo_nome) > 0: 
                        self._nome = novo_nome
                        print("Nome alterado com sucesso!")

                    else:
                        print("Nome inválido!")
                        print("Digite 1 para tentar novomente.")
                        print("Digite 2 para voltar ao menu principal.")

                        opcao = int(input("Indique a sua opção: "))

                        if opcao == 1:
                            print("Tentando novamente...")
                            time.sleep(2)
                            alterar_nome()

                        elif opcao == 2:
                            print("Retornando ao menu principal...")
                            time.sleep(2)


                try:
                    alterar_nome()

                except ValueError as a:
                    print("A sua opção deve ser descrita utilizando um número!")
                    print("Tentando novamente...")

                    time.sleep(2)

                    alterar_nome()

            elif opcao == 5:
                print("Encerrando operação...")
                time.sleep(2)


restaurante = Restaurante("Mc'donald")

print(restaurante.nome)
