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

    if(total != len(fila)): # a fila está cheia?
        fila[ultimo] = n # insercao na fila
        total = total +1 # incrementa o total de elementos na fila

        ultimo = ultimo + 1

        if ultimo == len(fila):
            ultimo = 0

    else:
        print("ERRO, FILA CHEIA")

def dequeue():
    print("removendo")
    global primeiro
    global fila
    global total
    elem = None
    if(total != 0): # está vazio?
            
        elem = fila[primeiro] #capturar o elemento no começo da fila (PRÓXIMO)
        fila[primeiro] = None #saiu da fila
        total = total - 1  # informa que a fila diminuiu

        primeiro = primeiro + 1
        if(primeiro == len(fila )):
            primeiro = 0
        
    else:
        print("Fila VAZIA")
        
    return elem

def listar_primeiro():
    global primeiro
    global fila
    print(fila[primeiro])



def listar_elementos():
    # for (int i = primeiro; i != ultimo; i++){
    #   
    #   i pode passar o tamanho da lista! 
    #   if (i passa do limite de indices){
    #       i = 0;  
    #   }
    #   printf("%d",lista[i]);
    # }
    global primeiro
    global ultimo
    global fila
    i = primeiro
    while(i != ultimo): # ultimo equivale a ultima posicao vazia
        if(i ==len(fila)):
            i = 0        
        print(fila[i])
        i = i+1

    
        

#zona de testes
queue("a")
print(fila)
print("ultima posicao livre: ",ultimo)
queue("b")
print(fila)
print("ultima posicao livre: ",ultimo)
queue("c")
print(fila)
print("ultima posicao livre: ",ultimo)
queue("d")
print(fila)
print("ultima posicao livre: ",ultimo)

print(dequeue())
print(fila)

print(dequeue())
print(fila)

print(dequeue())
print(fila)

print(dequeue())
print(fila)

print(dequeue())
print(fila)

queue("a")
print(fila)
queue("b")
print(fila)

print(dequeue())
print(fila)

queue("c")
print(fila)

print(dequeue())
print(fila)

queue("d")
print(fila)
queue("e")
print(fila)

print("primeiro: ",primeiro)
print("ultimo: ",ultimo)


listar_elementos()