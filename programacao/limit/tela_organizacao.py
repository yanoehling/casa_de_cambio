from programacao.limit.tela import Tela


class Tela_Organizacao(Tela):
    def tela_opcoes(self):
        print('-------ORGANIZAÇÕES-------')
        print('1 - Incluir organização')
        print('2 - Excluir organização')
        print('3 - Listar organização')
        print('4 - Alterar organização')
        print('0 - Retornar')

        opcao = int(input("Escolha uma Opção: "))
        return opcao

    def pegar_dados(self):
        print('-------CADASTRE SUA ORGANIZAÇÃO--------')
        nome = str(input('Digite o nome de sua Organização: '))
        id = str(input('Digite seu cnpj: '))
        return {"nome":nome, "id":id}
    
    def monstrar(self, dados_organizacao):
        print('--------INFORMAÇÕES--------')
        print(f'NOME DA ORGANIZAÇÃO: {dados_organizacao['nome']}')
        print(f'CNPJ DA ORGANIZAÇÃO: {dados_organizacao['id']}')
        print(f'CREDITO_USD DA ORGANIZAÇÃO: {dados_organizacao['credito_usd']}')

        print("\n")

    def selecionar(self):
        id = input('Digite o cnpj da organizacao que deseja achar: ')
        return id

    def mostra_msg(self, msg):
        return super().mostra_msg(msg)


        