class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


lista = None


def iniciaLista(itens):
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


def contaItens(lista):
    if lista == None:
        return 0
    else:
        contagem = 0
        indice = lista
        while indice != None:
            contagem += 1
            indice = indice.proximo
        return contagem


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

iniciaLista([1, 2, 3])

imprimeLista('Lista = ', lista)

print('Total de itens = %d' % contaItens(lista))
