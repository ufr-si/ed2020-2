class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


lista = None


def criaLista(itens):
    def add(i):
        global lista
        if lista == None:
            lista = No(i)
        else:
            aux = lista
            while aux.proximo != None:
                aux = aux.proximo

            novoItem = No(i)
            novoItem.anterior = aux
            aux.proximo = novoItem

    for i in itens:
        add(i)


def removeRepetidos():
    global lista
    if lista == None:
        print('Lista vazia')
    else:
        indice = lista
        while indice != None:
            subIndice = indice.proximo
            while subIndice != None:
                if subIndice.valor == indice.valor:
                    anterior = subIndice.anterior
                    proximo = subIndice.proximo
                    if anterior != None:
                        anterior.proximo = proximo
                    if proximo != None:
                        proximo.anterior = anterior

                    subIndice.proximo = None
                    subIndice.anterior = None

                    subIndice = proximo
                else:
                    subIndice = subIndice.proximo
            indice = indice.proximo


def imprimeLista(prefixo, lista):
    print('%s[ ' % prefixo, end='')

    aux = lista
    while aux != None:
        if aux.proximo == None:
            print('%d ' % aux.valor, end='')
        else:
            print('%d, ' % aux.valor, end='')
        aux = aux.proximo

    print(']')


# Main

criaLista([1, 1, 1])
imprimeLista('Lista = ', lista)

removeRepetidos()
imprimeLista('Lista limpa = ', lista)
