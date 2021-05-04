# o que vamos fazer ? 
# lista-sequencial 
import math
# inicializar estrutura
def inicializa_lista(n):
   return [None] * n

lista = inicializa_lista(10)

lista[0] = 1

#elementos validos
def elementos_validos(l):
    for i in range(0,len(l)): # percorreu TODA a lista
        if not l[i] is None: # se lista na posicao i nao eh "nada"
            print(l[i])
    pass

print ("elementos válidos: ")
elementos_validos(lista)
print()

#exibir elementos
def print_lista(l):
    print("imprimindo lista")
    for i in range(0,len(l)):
        print(l[i])

print_lista(lista)

def add_elemento(l,el,pos):
    print("adicionando elemento")
    # posicao existe? 
    tamanho = len(l)
    ultima_posicao = tamanho-1
    # se posicao informada é maior que ultima_posicao OU pos < 0 
    ## posicao invalida!!!
    if pos > ultima_posicao or pos >0:
        return -1 # erro!
    else:
        #posso adicionar! 
        # esse elemento (el) já existe na lista?
        for i in range(0,tamanho): # percorra toda a lista e 
            if el == l[i]: # elemento que eu vou adicionar está na lista? 
                return -1 #retorna erro!
        
        # o elemento não está na lista! 

        # tem alguma coisa nessa posicao? 
        if not l[pos] is None:
            # ENTRA SE TEM ALGUMA COISA (ou seja, se não é NONE)
            #TODO: caso Isaias  (verificar se tem algum valor na posicao; se sim, movemos os valores para as posicoes subsequentes.)
            return -1 #retorna erro!
        else:
            l[pos] = el

    return 0


add_elemento(lista,5)

def del_elemento(n):
    # elemento existe? 
    # o que eu faco depois que removo da lista? 
    # o que mais de restricao posso ter? 

    pass     

def busca_elemento(lista,n):
    #percorre até achar
    for i in range (0,len(lista)):
        if(lista[i] == n):
            return i
    return -1

### RESTRICAO: lista tem que estar ordenada para esse funcionar
# o que é ? 
# como se comporta? 
#lista_telefonica!
def busca_binaria(lista,x):
    inf = 0
    sup = len(lista)-1
    while inf <= sup:
        calc = inf + sup /2
        meio = math.floor(calc)
        if lista[meio] == x:
            return meio
        else:
            if lista[meio] < x:
                inf = meio +1
            else:
                # lista[meio] > x
                sup = meio-1
    return -1

# o que mais podemos fazer? 
# inverter
# ordenar
# verificar (e remover) duplicados 
