from math import e
from time import sleep
import numpy as np
from tabulate import tabulate
from DeterministicSimulation import DeterministicSimulation
from RandomSimulationMM2 import RandomSimulationMM2
from RandomSimulationMM1 import RandomSimulationMM1



def menu():
    print("\nChoose an option: ")
    print("1: Deterministc Simulation:")
    print("2: Random Simulation - MM1")
    print("3: Random Simulation - MM2")
    return

def sub_menu():
    print("\nChoose an option: ")
    print("1: With queue limit")
    print("2: Without queue limit")
    return



if  __name__ == "__main__":
    
    menu()
    option = int(input())
    sub_menu()
    option2 = int(input())

    if(option == 1):
        S = DeterministicSimulation(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    elif (option ==2):
        S = RandomSimulationMM1(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    else:
        S = RandomSimulationMM2(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Nº Servidor","Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))

    S.calculateStatistics()



    