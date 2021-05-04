#o que faz uma fila ser uma fila ? 
# FIRST IN, FIRST OUT (Primeiro Que entra, Primeiro que sai)


fila = [None]*4
# 0,1,2,3
#  , , , . 
primeiro = 0
ultimo = 0
total = 0

def queue(n):
    print("tentando adicionar ",n)
    global ultimo
    global fila
    global total

    if(total != len(fila)):
        fila[ultimo] = n
        total = total +1

        if ultimo == len(fila)-1:
            ultimo = 0
        else:
            ultimo = ultimo + 1        
    else:
        print("ERRO, FILA CHEIA")

def dequeue():
    print("removendo")
    global primeiro
    global fila
    global total
    elem = None
    if(total != 0):
            
        elem = fila[primeiro]
        fila[primeiro] = None
        total = total - 1 
        if primeiro == len(fila) -1: 
            primeiro = 0
        else:
            primeiro = primeiro +1
    else:
        print("Fila VAZIA")
        
    return elem
        

#zona de testes
queue("a")
print(fila)
queue("a")
print(fila)
queue("a")
print(fila)
queue("a")
print(fila)
queue("a")
print(fila)

print("removi: ",dequeue())
print(fila)
print("removi: ",dequeue())
print(fila)
print("removi: ",dequeue())
print(fila)
print("removi: ",dequeue())
print(fila)
print("removi: ",dequeue())
print(fila)

print("primeiro, ",primeiro)
print("ultimo, ",ultimo)
print("total, ",total)

queue("a")
print(fila)
queue("b")
print(fila)
queue("c")
print(fila)
print("removi: ",dequeue())
print(fila)
print("removi: ",dequeue())
print(fila)
queue("d")
print(fila)
