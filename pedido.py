from datetime import datetime
import funcoes 
from prato import Prato
import random
import time

class Pedido:
    def __init__(self, cardapio):
        self._codigo = funcoes.gerar_codigo()
        self._cardapio = cardapio
        self._pratos = []
        self._valor = 0
        self._inicio_pedido = None 
        self._fim_pedido = None

    def iniciar_pedido(self):
        # print("Indique a quantidade de pratos que você ")

        # quantidade_pratos_adicionar = int(input("Indique a quantidade de pratos que você gostaria de adicionar: "))

        # quantidade_adicionada = 0
        # while quantidade_pratos_adicionar < quantidade_adicionada:
        #     nome

        def pedindo():
            print("Digite 1 para ver o cardápio.")
            print("Digite 2 para adicionar um prato ao pedido.")
            print("Digite 3 para remover algum prato.")
            print("Digite 4 para pagar.")
            print("Digite 5 para encerrar operação.")

            opcao_a = int(input("Indique a sua opção: "))

            if opcao_a == 1:
                for item in self._cardapio:
                    item.mostrar_prato()
                    print("")

                pedindo()

            elif opcao_a == 2:
                print("Adicionando prato!")
                time.sleep(2)
                nome_prato = input("Indique o nome do prato que você gostaria de adicionar ao pedido: ")

                for prato_a in self._cardapio:
                    # if prato.nome.lower() == nome_a.lower():
                    if prato_a.nome == nome_prato:
                        self._pratos.append(prato_a)
                        self._valor += prato_a.preco 

                        print("Prato adicionado com sucesso!")
                        time.sleep(2) 
                        pedindo()

                    # else:
                    #     print("Prato não encontrado!")
                    #     print("Voltando ao menu!")
                    #     print("...")
                    #     time.sleep(2)
                    #     pedindo()

            elif opcao_a == 3:
                print("Removendo prato do pedido...")
                time.sleep(2)

                nome = input("Indique o nome do prato que você gostaria de remover do pedido: ")
                for prato in self._pratos:
                    if prato.nome == nome:
                        self._pratos.remove(prato)
                        self._valor -= prato.preco
                        print("Prato removido com sucesso!")
                        print("...")
                        time.sleep(2)
                        pedindo()
                else:
                    print("Este prato não está no pedido!")
                    print("Voltando ao menu...")
                    time.sleep(2)
                    pedindo()

            elif opcao_a == 4:
                def pagando():
                    print(f"Valor: {self._valor}")
                    print(f"""Digite 1 para pagar com débito.
Digite 2 para pagar com crédito.""")

                    opcao = int(input("Indique a forma de pagamento: "))

                    if opcao == 1:
                        print("Débito selecionado...")
                        time.sleep(2)

                        numero = int(input("Indique o número do cartão: "))
                        senha = int(input("Indique a senha: "))

                        print("Pagamento concluído...")
                        time.sleep(2)
                        pedindo()

                    elif opcao == 2:
                        print("Crédito selecionado...")
                        time.sleep(2)

                        numero = int(input("Indique o número do seu cartão de crédito: "))
                        senha = int(input("indique a sua senha: "))

                        # Pagando 
                        print("Analizando...")
                        time.sleep(2)

                        print("Pagamento conluído...")
                        time.sleep(2)
                        pedindo()

                    else:
                        print("Opção inválida!")
                        print("Tentando novamente...")

                        pagando()

                try:
                    pagando()

                except ValueError as a:
                    print(a)
                    print("O formato de pagamento deve ser descrito utilizando um número.")
                    print("""O número do cartão de crédito e a senha devem descritos utilizando 
um tipo de dados inteiro.""")
                    time.sleep(2)
                    print("Tentando novamente...")
                    time.sleep(2)
                    pagando()

            elif opcao_a == 5:
                print("Encerrando o sistema...")

                for prato in self._pratos:
                    print(prato.mostrar_prato())

                print(f"Valor: {self._valor}")

                self._fim_pedido = datetime.now()
                print(f"""Início pedido: {self._inicio_pedido}
Termino pedido: {self._fim_pedido}""")

            else:
                print("Opção inválida...")
                time.sleep(2)
                print("Tentando novamente...")
                time.sleep(2)
                pedindo()

        try:
            self._inicio_pedido = datetime.now()
            pedindo()



        except ValueError as a:
            print(a)
            print("A sua opção deve ser descrita utilizando um tipo de dados numérico!")
            print("Tentando novamente...")
            time.sleep(2)
            pedindo()



cardapio = []
nome_pratos = ["Pizza", "Hámburguer", "Sorvete", "Chocolate", "Refrigerante", "Lasanha"]
for a in range(5):
    nome = random.choice(nome_pratos)
    preco = float(random.randint(10, 14))
    prato = Prato(nome, preco)

    cardapio.append(prato)


for prato in cardapio:
    if prato.nome == "Lasanha":
        print("Prato")
pedido = Pedido(cardapio)

pedido.iniciar_pedido()