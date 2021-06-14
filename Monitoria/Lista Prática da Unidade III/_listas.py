class No:
    def __init__(self, valor):
        self.proximo = None
        self.valor = valor


class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def add(self, n):
        if (self.topo == None):
            self.topo = No(n)
        else:
            novoItem = No(n)
            novoItem.proximo = self.topo
            self.topo = novoItem

    def remove(self):
        if (self.topo == None):
            print('Pilha Vazia')
        else:
            self.topo = self.topo.proximo

    def print(self):
        if (self.topo == None):
            print('Pilha Vazia')
        else:
            indice = self.topo
            while indice != None:
                print(indice.valor)
                indice = indice.proximo


class FilaEncadeada:
    def __init__(self):
        self.inicio = None

    def add(self, n):
        if (self.inicio == None):
            self.inicio = No(n)
        else:
            indice = self.inicio
            while indice.proximo != None:
                indice = indice.proximo
            indice.proximo = No(n)

    def remove(self):
        if (self.inicio == None):
            print('Fila Vazia')
        else:
            self.inicio = self.inicio.proximo

    def print(self):
        if (self.inicio == None):
            print('Fila Vazia')
        else:
            indice = self.inicio
            while indice != None:
                print(indice.valor)
                indice = indice.proximo


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def add(self, n):
        novoItem = No(n)
        if (self.inicio == None):
            self.inicio = novoItem
        else:
            indice = self.inicio
            while indice.proximo != None:
                indice = indice.proximo
            indice.proximo = novoItem

    def remove(self, n):
        if (self.inicio == None):
            print('Lista Vazia')
        elif (self.inicio.proximo == None):
            if (self.inicio.valor == n):
                self.inicio = None
            else:
                print('Esse item não foi encontrado')
        else:
            indiceAnterior = self.inicio
            indice = self.inicio
            while indice != None:
                if indice.valor == n:
                    indiceAnterior.proximo = indice.proximo
                    return
                else:
                    indiceAnterior = indice
                    indice = indice.proximo
            print('Esse item não foi encontrado')

    def print(self):
        if (self.inicio == None):
            print('Lista Vazia')
        else:
            indice = self.inicio
            while indice != None:
                print(indice.valor)
                indice = indice.proximo
