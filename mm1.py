import random

def menu():
    print("\n1: Numero medio de clientes na fila esperando atendimento")
    print("2: Tempo medio gasto por um cliente no sistema")
    print("3: Numero de clientes atendidos por hora")
    print("4: Probabilidade de se ter X clientes no sistema")
    print("0: Sair\n")

def menuConfig():
    print("\n1: Tempo entre Chegadas (TEC) ser determinístico ou aleatório")
    print("2: Tempo de serviço (TS) ser determinístico ou aleatório")
    print("3: Fila com ou sem limite\n")

def calculo_L(lambida, mi):
    #Media do numero de clientes presentes em todo o sistema
    l = (lambida / (lambida/mi))
    return l


def calculo_LQ(lambida, mi):
    #Numero medio de clientes na fila esperando atendimento
    lq = ((lambida/mi) * (lambida/mi)) / (1-(lambida/mi))
    return lq

def calculo_LS(lambida, mi):
    #Numero medio de clientes em atendimento
    ls = (lambida/mi)
    return ls

def calculo_W(lambida, mi):
    #Tempo medio gasto por um cliente no sistema
    l = calculo_L(lambida, mi)
    w = l / lambida
    return w

def calculo_pi(lambida, mi, clientes_no_sistema):
    #Probabilidade de X clientes no sistema em determinado momento
    p = (lambida/mi)
    if (clientes_no_sistema == 0):
        return (1 - p)
    else:
        return ((p ** clientes_no_sistema) * (1-p))
   
def main():

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("SIMULAÇÃO DE SISTEMA M/M/1")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    

    print("Determinar tempo entre chegadas (TEC):")
    print("1: Deterministico")
    print("2: Aleatorio")
    num = int(input())
    if( num == 1):
        tec = int(input("Entre com TEC (tempo entre chegadas de clientes) em minutos: "))
        lambida = 60/tec
        print("Tem-se que chegam {} clientes por hora".format(lambida))

    if( num == 2):
        tec = random.randint(5, 20)
        print("TEC = {}".format(tec))
        lambida = 60/tec
        print("Tem-se que chegam {} clientes por hora".format(lambida))
    
    print("Determinar tempo de serviço (TS):")
    print("1: Deterministico")
    print("2: Aleatorio")
    num2 = int(input())
    if( num2 == 1):
        ts = int(input("Entre com TS (tempo de serviço para cada cliente) em minutos: "))
        mi = 60/ts
        print("São atendidos {} clientes por hora".format(mi))

    if( num2 == 2):
        ts = random.randint(5, 20)
        print("TS = {}".format(ts))
        mi = 60/ts
        print("São atendidos {} clientes por hora".format(mi))


    print("OPÇÕES: ")
    option = -1
    while(option != 0):
        menu()
        option = int(input("Digite uma opcao: "))
        if(option == 1):
            print(calculo_LQ(lambida, mi))
        elif(option == 2):
            print(calculo_W(lambida, mi))
        elif(option == 3):
            print((lambida/mi)*mi)
        elif(option == 4):
            clientes_no_sistema = int(input("Entre com o valor de X: "))
            print("A probabilidade de se ter {} no sistema eh: {}".format(clientes_no_sistema, calculo_pi(lambida, mi, clientes_no_sistema)))
        else:
            print("Digite uma opcao válida!")


if __name__ == "__main__":
    main()