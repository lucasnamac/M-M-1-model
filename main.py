from DeterministicSimulation import Deterministic_Simulation
from RandonSimulation import Random_Simulation


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






    







    