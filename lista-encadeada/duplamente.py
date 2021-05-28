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
            no = No(n) # criei o nó
            lista.anterior = no 
            no.proximo = lista 
            lista = no
        else: # n > lista.item 
            aux = lista
            while aux.proximo != None and aux.proximo.item <= n:
                aux = aux.proximo
            # ? aux >= n
            if aux.item == n:    
                no = No(n) # criei nó
                no.proximo = aux
                no.anterior = aux.anterior
                aux.anterior.proximo = no
                aux.anterior = no
            elif n>aux.item: 
                no = No(n)
                aux.proximo = n
                no.anterior = aux
                no.proximo = None

def imprime_lista():
    global lista
    # enquanto o proximo elemento nao for None: imprime o elemento atual
    aux = lista
    print("Lista:")
    while aux != None: 
        print(aux,",")
        aux = aux.proximo

inserir_ordenado(50)
inserir_ordenado(40)
inserir_ordenado(30)
inserir_ordenado(50)
inserir_ordenado(60)
inserir_ordenado(70)

imprime_lista()