from math import e
from time import sleep
import numpy as np
from tabulate import tabulate
from DeterministicSimulationMM1 import DeterministicSimulationMM1
from DeterministicSimulationMM2 import DeterministicSimulationMM2
from RandomSimulationMM2 import RandomSimulationMM2
from RandomSimulationMM1 import RandomSimulationMM1



def menu():
    print("\nChoose an option: ")
    print("1: Deterministc Simulation - M|M|1:")
    print("2: Deterministc Simulation - M|M|2:")
    print("3: Random Simulation - M|M|1")
    print("4: Random Simulation - M|M|2")
    print("0: Exit")
    return

def sub_menu():
    print("\nChoose an option: ")
    print("1: With queue limit")
    print("2: Without queue limit")
    return



if  __name__ == "__main__":
    
    menu()
    option = int(input())
    if(option == 0):
        print("Obrigado!")
        exit()
    sub_menu()
    option2 = int(input())

    if(option == 1):
        S = DeterministicSimulationMM1(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    elif (option ==2):
        S = DeterministicSimulationMM2(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    elif (option == 3):
        S = RandomSimulationMM1(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Nº Servidor","Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    elif (option == 4):
        S = RandomSimulationMM2(option2)
        print(tabulate(S.data,headers = ["Evento", "Cliente", "Tempo no relógio", "Nº Servidor","Estado do servidor", "Tamanho da fila", "Horário de chegada", "Horário de saída"], tablefmt="presto"))
    S.calculateStatistics()



    