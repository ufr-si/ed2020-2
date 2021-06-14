class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


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
            aux.proximo = No(i)

    for i in itens:
        add(i)


def removeRepetidos():
    global lista
    if lista == None:
        print('Lista vazia')
    else:
        indice = lista
        while indice != None:
            subIndiceAnt = indice
            subIndice = indice.proximo
            while subIndice != None:
                if subIndice.valor == indice.valor:
                    subIndiceAnt.proximo = subIndice.proximo
                subIndiceAnt = subIndice
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

criaLista([1, 2, 3, 4, 1, 3, 2, 4])
imprimeLista('Lista = ', lista)

removeRepetidos()
imprimeLista('Lista limpa = ', lista)
