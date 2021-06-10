class No:
  def __init__(self, item=None, proximo=None, anterior = None):
    self.item = item
    self.proximo = proximo
    self.anterior = anterior

    # funcao que serve para imprimir o que eu quiser quando eu chamo print no item
    # desse TAD (Tipo Abstrato de Dados)
  def __str__(self):
    return str(self.item)

lista = None

def inserir_ordenado(n):
    
    global lista
    if lista == None:
        no = No(n)
        lista = no
    else:
        # o elemento pode ser maior, igual, pode ser menor
        if n <= lista.item: 
            # elemento é menor!
            no = No(n) # criei o nó
            lista.anterior = no # anterior do item na lista acessa o nó
            no.proximo = lista 
            lista = no #ele vira o topo da lista
        else: # n > lista.item 
            # preciso percorrer até quando ele for menor (ou for o fim da lista)
            aux = lista
            #enquanto nao for o último item da lista (aux.proximo = None)
            # e o item for menor ou igual a n
            while aux.proximo != None and aux.item < n: 
                aux = aux.proximo #pegue o próximo  
            
            # cheguei no aux aonde eu colocarei o item depois
            # sr aux prox vazio, item no final
            print("tipo aux ", type(aux))
            print("tipo aux ", type(aux.proximo))
            if aux.proximo == None:
                
                #inserindo no final
                no = No(n)
                aux.proximo = no
                
                no.anterior = aux
                no.proximo = None
                
            else:
                #nao é no final, vou ter que colocar no meio!!
                no = No(n) # criei nó
                no.proximo = aux #guarde o próximo
                no.anterior = aux.anterior # anterior do aux vira anterior do novo no
                aux.anterior.proximo = no # o próximo do anterior do aux aponta pra no
                aux.anterior = no    # aux anterior aponta para no.
                
def imprime_lista():
    global lista
    # enquanto o proximo elemento nao for None: imprime o elemento atual
    aux = lista
    print("Lista:")
    while aux != None: 
        print(aux,",")
        aux = aux.proximo 

a = input("O que fazer? ")
while a != 0:
    if a =="1":
        b = input("Numero a inserir")
        inserir_ordenado(b)
        imprime_lista()

    if( a == "2"):
        exit()
    a = input("O que fazer? ")


