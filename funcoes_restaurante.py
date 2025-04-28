
import time
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
                        


