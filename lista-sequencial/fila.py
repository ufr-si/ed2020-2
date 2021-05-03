#o que faz uma fila ser uma fila ? 
# FIRST IN, FIRST OUT (Primeiro Que entra, Primeiro que sai)


fila = [None]*4
# 0,1,2,3
#  , , , . 
primeiro = 0
ultimo = 0
qtde = 0

def queue(n):
    global ultimo
    global capacidade
    global fila
    if(qtde == len(fila)):
        print("ERRO, FILA CHEIA")
        return -1
    else:
        fila[ultimo]=n
        qtde = qtde +1 
        #alterar o valor de ultimo
        if ultimo == len(fila)-1:
            ultimo = 0
        else:
            ultimo = ultimo +1
        return 0

def dequeue():
    global primeiro
    global capacidade
    global fila
    if capacidade > 0: # posso remover ? tem elemento?
        elem = fila[primeiro] #removo
        fila[primeiro] = None
        capacidade = capacidade - 1
        if primeiro +1 > len(fila)-1: # se eu tiver jogando muito pra frente
            primeiro=0 # volto pro zero 
        else:
            primeiro = primeiro +1
    else:
        print("ERRO, FILA VAZIA!")
        return None
    return elem 
    pass


queue("a")
print(fila)
queue("b")
print(fila)
queue("c")
print(fila)
queue("d")
print(fila)

print(dequeue())
print(fila)
print(dequeue())
print(fila)
print(dequeue())
print(fila)
print(dequeue())
print(fila)
dequeue()
dequeue()
dequeue()
