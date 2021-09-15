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

    lambida = int(input("Entre com o numero de clientes que chegam por hora no sistema (λ): "))
    mi = int(input("Entre com o numero de clientes atendidos por hora no sistema (μ): "))

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
            print("Difite uma opcao válida!")


if __name__ == "__main__":
    main()