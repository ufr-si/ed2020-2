class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


lista = None


def criaLista(itens):
    def add(valor):
        global lista
        if lista == None:
            novoValor = No(valor)
            novoValor.proximo = novoValor
            lista = novoValor
        else:
            aux = lista
            while aux.proximo != lista:
                aux = aux.proximo

            novoValor = No(valor)
            novoValor.proximo = lista
            aux.proximo = novoValor

    for valor in itens:
        add(valor)


def removeRepetidos(lista):
    if lista == None:
        print('Lista vazia')
    elif lista.proximo == lista:
        print('Lista contem apenas 1 elemento')
    else:
        indice = lista
        while indice.proximo != lista:
            subIndiceAnt = indice
            subIndice = indice.proximo
            while subIndice != lista:
                if subIndice.valor == indice.valor:
                    subIndiceAnt.proximo = subIndice.proximo
                    subIndice.proximo = None
                    subIndice = subIndiceAnt.proximo
                else:
                    subIndice = subIndice.proximo
            indice = indice.proximo


def imprimeLista(prefixo, lista):
    print('%s[ ' % prefixo, end='')

    if lista == None:
        pass
    if lista.proximo == lista:
        print('%d ' % lista.valor, end='')
    else:
        aux = lista
        while aux.proximo != lista:
            print('%d, ' % aux.valor, end='')
            aux = aux.proximo
        print('%d ' % aux.valor, end='')

    print(']')


# Main

criaLista([1, 1, 3])
imprimeLista('Lista = ', lista)

removeRepetidos(lista)
imprimeLista('Lista limpa = ', lista)
