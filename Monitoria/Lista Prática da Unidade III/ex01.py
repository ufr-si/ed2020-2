class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


listaDada = None
listaOrdenada = None


def criaListaData(itens):
    def add(n):
        global listaDada
        if listaDada == None:
            listaDada = No(n)
        else:
            aux = listaDada
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = No(n)

    for i in itens:
        add(i)

def criaListaOrdenada():
    def getMax():
        global listaDada
        if listaDada == None:
            return None
        elif listaDada.proximo == None:
            maior = listaDada
            listaDada = None
            return maior
        else:
            anteriorAoMaior = None
            maior = listaDada

            indiceAnterior = listaDada
            indice = listaDada
            while indice != None:
                if indice.valor > maior.valor:
                    anteriorAoMaior = indiceAnterior
                    maior = indice

                indiceAnterior = indice
                indice = indice.proximo

            if (anteriorAoMaior != None):
                anteriorAoMaior.proximo = maior.proximo
            else:
                listaDada = maior.proximo

            return maior

    def insert(novoValor):
        global listaOrdenada
        novoValor.proximo = listaOrdenada
        listaOrdenada = novoValor

    aux = getMax()
    while aux != None:
        insert(aux)
        aux = getMax()


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

criaListaData([5, 4, 3, 2, 1])
imprimeLista('Lista dada = ', listaDada)

criaListaOrdenada()
imprimeLista('Lista ordenada = ', listaOrdenada)
