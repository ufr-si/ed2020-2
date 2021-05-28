# typedef struct { int item; Node prox*;} Node;
# No no; 
# no.item = 10

lista = "" ### str

class No:
  def __init__(self, item=None, proximo=None, anterior = None):
    self.item = item
    self.proximo = proximo
    self.anterior = anterior

    # funcao que serve para imprimir o que eu quiser quando eu chamo print no item
    # desse TAD (Tipo Abstrato de Dados)
  def __str__(self):
    return "Valor do no: " + str(self.item)+"\n"

# criacao? 
def criar_lista(val):
    return No(val)

# insercao ? 

#pilha!
def push(val):
    global lista
    # cria o nó 
    no = No(val)
    no.proximo = lista
    lista = no # lista passa a APONTAR para o nó NOVO. 
    
def imprime_lista():
    global lista
    # enquanto o proximo elemento nao for None: imprime o elemento atual
    aux = lista
    while aux != None: 
        print("Imprimindo:", aux)
        aux = aux.proximo
        
# remocao?
def pop(): # desenfileira
    global lista

    aux = lista
    lista = lista.proximo 
    aux.proximo = None
    aux = aux.item
    return aux

def enfileira(n):
    global lista

    # criar um novo nó
    no = No(n)
    # percorrer nossa lista até achar o último elemento
    if lista != "":
        aux = lista
        while aux.proximo != None: # percorre até achar o próximo vazio.
            aux = aux.proximo
        # nesse ponto, eu encontrei o aux que era
        # o último elemento.
        # agora posso adicionar o no novo na última posicao
        aux.proximo = no # adicionei
    else:
        lista = No(n)
    # adicionar o elemento novo na última posição


# busca ?



#fila ? 

# # main
# val = 10
# lista = criar_lista(val)
# val = 20
# push(val)
# val = 30
# push(val)

# print("Elemento removido",remover())

# imprime_lista()

enfileira(10)
enfileira(20)
enfileira(30)

imprime_lista()
