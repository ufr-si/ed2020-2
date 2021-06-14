class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


deque = None


def inserir(n, posicao):
    global deque
    if deque == None:
        deque = No(n)
    else:
        if posicao == 'inicio':
            novoItem = No(n)
            novoItem.proximo = deque
            deque = novoItem
        else:
            indice = deque
            while indice.proximo != None:
                indice = indice.proximo
            indice.proximo = No(n)


def remover(posicao):
    global deque
    if deque == None:
        print('Deque Vazio')
    else:
        if posicao == 'inicio':
            deque = deque.proximo
        else:
            indiceAnt = deque
            indice = deque
            while indice.proximo != None:
                indiceAnt = indice
                indice = indice.proximo

            indiceAnt.proximo = indice.proximo
            indice.proximo = None  # free


def imprimeDeque(prefixo, deque):
    print('%s[ ' % prefixo, end='')

    aux = deque
    while aux != None:
        if aux.proximo == None:
            print('%d ' % aux.valor, end='')
        else:
            print('%d, ' % aux.valor, end='')
        aux = aux.proximo

    print(']')


# Main

# Testar inserções
for valor, posicao in [(2, 'inicio'), (3, 'final'), (4, 'final'), (1, 'inicio')]:
    inserir(valor, posicao)
    imprimeDeque('inserir(%d, %s) \t= ' % (valor, posicao), deque)

imprimeDeque('deque = ', deque)

# Testar remoção
for posicao in ['inicio', 'final', 'final', 'inicio', 'inicio', 'final']:
    remover(posicao)
    imprimeDeque('remover(%s) = ' % posicao, deque)

imprimeDeque('deque = ', deque)
