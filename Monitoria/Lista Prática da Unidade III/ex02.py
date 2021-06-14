class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


L1 = None
L2 = None


def criaL1(itens):
    def add(i):
        global L1
        if L1 == None:
            L1 = No(i)
        else:
            aux = L1
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = No(i)

    for i in itens:
        add(i)


def criaL2(itens):
    def add(i):
        global L2
        if L2 == None:
            L2 = No(i)
        else:
            aux = L2
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = No(i)

    for i in itens:
        add(i)


def concatena():
    global L1
    global L2
    if L1 == None:
        L1 = L2
    else:
        aux = L1
        while aux.proximo != None:
            aux = aux.proximo
        aux.proximo = L2


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

criaL1([1, 2, 3, 4])
criaL2([5, 6])

imprimeLista('L1 = ', L1)
imprimeLista('L2 = ', L2)

concatena()
imprimeLista('L1 + L2 = ', L1)
