# o que faz uma pilha ser pilha?
# LAST IN, FIRST OUT (LIFO)

pilha = [None]*4 # lista estáticas, tamanho fixo


topo = -1 # indica aonde está o topo da pilha; -1 indica que a pilha está vazia 

# def vazia():
#     global topo
#     if topo == -1:
#         return True
    
#     return False

def push(n):
    global topo
    # SE A PILHA ESTÁ CHEIA, NÃO POSSO INSERIR!
    if not topo == len(pilha)-1:
        topo = topo +1
        pilha[topo] = n    
        print("Adicionado: ", n)
    else:
        print("ERRO, ESTOURO DE PILHA KABUUUUUUM paga a gente")

def pop():
    global topo # 9
    global pilha # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # se a pilha nao esta vazia
    if topo == -1: 
        return "PILHA VAZIA!"
    else:
        rem = topo # 9
        elemento = pilha[rem] # pilha[9] = 10 
        pilha[topo] = None # [1, 2, 3, 4, 5, 6, 7, 8, 9, None]
        topo = topo-1 # 8
        print(rem)
        return elemento
    
push(1)
push(2)
push(3)
push(4)
push(5)


print(pilha)


print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)

push(1)
push(2)
print(pilha)
print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)
print("Removi: ", pop())
print(pilha)