# Faca um programa que receba
# dados de uma venda (produtos,
# quantidades, valor),
# armazenando e informando o valor 
# final da compra e os produtos 
# adquiridos (como em um cupom fiscal)

# struct{
#  int quantidade;
#  char produto[100];
#  float valor;
# }

def exercicio_1():
    lista_produtos = [] # vetor vazio

    quero_comprar = input("Quer comprar?\n")
    # enquanto eu quiser comprar 
    soma = 0
    while quero_comprar == "S" or quero_comprar == "s":
        # scanf("%c",produto); 
        produto = input("Produto:  ")
        qtde = int(input("qtde: "))
        valor = float(input("valor: "))
        a = {"produto":produto,"qtd":qtde,"valor":valor}
        lista_produtos.append(a) # adicionando item no vetor
        # adiciono produtos na lista
        quero_comprar = input("Ainda quer comprar?\n")
        soma = soma + item["valor"]*item["qtd"]


    print("Resultado final:",soma)

# multiplicar 
# 3*2 = 2+2+2
# 2*3 = 3+3

# m, multiplicado n vezes
# m = 3, n=1
def mult(m,n):
    if(n==1):
        return m
    else:
        # m = 3, n-1 = 0
       return m+mult(m,n-1)

print(mult(2,3))

#4! = 4*3*2*1
# 4! = 4* 3!
# 3! = 3* 2!
# 2! = 2*1!
# 1! = 1

def fat(n):
    if(n==1):
        return 1
    else:
        return n * fat(n-1)

def leia_do_arquivo(n):
    f = open(n,"r") # abrir o arquivo
    print(f.readlines())
    f.close()
    leia_do_arquivo("teste")
