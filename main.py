from DeterministicSimulation import Deterministic_Simulation
from RandonSimulator import Random_Simulation



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


def menu():
    print("\nChoose an option: ")
    print("1: Deterministc Simulation")
    print("2: Random Simulation ")
    print("0: Exit")
    return

if  __name__ == "__main__":
    
    menu()
    option = int(input())

    if(option == 1):
        Deterministic_Simulation()
    else:
        Random_Simulation()






    







    