#Definindo a classe Nodo (Nó)
class Nodo:
    def __init__(self, cor, numero):
        self.cartao = [cor, numero] #Lista com a cor e número do cartão do paciente
        self.proximo = None #Aponta para o próximo nodo

class ListaEncadeada:
    def __init__(self):
        self.head = None #Iniciando a lista vazia

    def inserirSemPrioridade(self, nodo): #Inserindo o nodo no final da lista (Sem prioridade)
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo): #Inserindo o nodo no inicio da lista (Com prioridade)
        if not self.head:
            self.head = nodo
        else:
            if self.head.cartao[0] == 'V': #Verifica se o primeiro nodo tem a cor Verde
                nodo.proximo = self.head
                self.head = nodo
            else:
                atual = self.head
                while atual.proximo and atual.proximo.cartao[0] == 'A': #O novo nodo é inserido antes do Verde
                    atual = atual.proximo
                nodo.proximo = atual.proximo
                atual.proximo = nodo

    def inserir(self, corCartao, numCartao): #Método de inserir na lista
        novo_nodo = Nodo(corCartao, numCartao)
        if not self.head:
            self.head = novo_nodo
        elif corCartao == 'V':          #Insere o nodo sem prioridade
            self.inserirSemPrioridade(novo_nodo)
        elif corCartao == 'A':          #Insere o nodo com prioridade
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):      #Armazena e mostra a lista de espera dos pacientes
        if not self.head:
            print("A fila está vazia.")
        else:
            atual = self.head
            print("LISTA -> ", end="")  #Apresenta na tela a lista dos atuais pacientes
            while atual:
                print(f"[{atual.cartao[0]} , {atual.cartao[1]}]", end=" ")
                atual = atual.proximo
            print()

    def atenderPaciente(self): #Atende e remove o primeiro paciente da lista
        if not self.head:
            print("Não há pacientes na fila.")
        else:
            print(f"Atendendo o paciente cartão cor {self.head.cartao[0]} e número {self.head.cartao[1]}.")
            self.head = self.head.proximo

# PROGRAMA PRINCIPAL
lista_espera = ListaEncadeada()

while True:
    print("1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - SAIR")

    op = int(input("\nEscolha uma opção: "))
    if op == 1:
        corCartao = input("Informe a cor do cartão (A/V): ").upper()
        numCartao = int(input("Informe o número do cartão: "))
        lista_espera.inserir(corCartao, numCartao)
    elif op == 2:
        lista_espera.imprimirListaEspera()
    elif op == 3:
        lista_espera.atenderPaciente()
    elif op == 4:
        print("Finalizando programa...")
        break
    else:
        print("Opção Inválida!\n")
