# o que faz uma pilha ser pilha?
# LAST IN, FIRST OUT (LIFO)

pilha = [None]*50 # lista estáticas, tamanho fixo

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
        
    else:
        print("ERRO, ESTOURO DE PILHA KABUUUUUUM paga a gente")

def pop():
    global topo # 9
    global pilha # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    if topo == -1: 
        return -1
    else:
        # se a pilha nao esta vazia
        rem = topo # 9
        elemento = pilha[rem] # pilha[9] = 10 
        pilha[topo] = None # [1, 2, 3, 4, 5, 6, 7, 8, 9, None]
        topo = topo-1 # 8
        return elemento

def converte_decimal_binario(n):
    
    binario = ""
    quociente = 0
    resto = 0
    # push no n
    push(n)

    n = pop()
    while n != 0:
        quociente = n//2
        resto = n % 2 
        push(resto)
        push(quociente)
        n = pop() # pop de novo pra pegar o próximo n  
    
    n = pop()
    while(n !=-1):
        binario = binario+str(n)
        n = pop()

    return binario

#n = input("Diga o numero ")

# print(converte_decimal_binario(int(n)))


def palindromo(palavra):
    # ler caractere por caracter
    # adicionar na pilha 
    
    
    for c in palavra:
        # ignorar espacos e pontos
        if( c not in ['.',' ']):
            push(c)
    
    for c in palavra:    
        if( c not in ['.',' ']):
            n = pop()
            if (n != c):
                return False
    
    return True

s = input("Digite uma palavra: ")
if palindromo(s):
   print("É palindromo!") 
else:
    print("não é palindromo!")
