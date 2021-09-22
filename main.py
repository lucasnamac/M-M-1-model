from math import e
import numpy as np
from numpy.random.mtrand import poisson
from tabulate import tabulate
from DeterministicSimulation import Deterministic_Simulation_lucas
from RandonSimulation import Random_Simulation
import Deterministic_Simulation_01


def menu():
    print("\nChoose an option: ")
    print("1: Deterministc Simulation Versao 1")
    print("2: Deterministc Simulation Versao 2")
    print("3: Random Simulation")
    return



if  __name__ == "__main__":
    
    menu()
    option = int(input())

    if(option == 1):
        S = Deterministic_Simulation_lucas()
    if(option == 2):
        Deterministic_Simulation_01.main()
    else:
        S = Random_Simulation()



    