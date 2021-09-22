from math import e
import numpy as np
from numpy.random.mtrand import poisson
from tabulate import tabulate
import random


def menu():
    print("\nChoose an option: ")
    print("1: Deterministc Simulation")
    print("2: Random Simulation")
    return

class Deterministic_Simulation:
    TR=0
    ES=0
    TF=0
    HC=0
    HS=9999

    data=[[]] 

    def processArrival(self, TEC, TS):
        self.TR=self.HC
        if self.ES==0 :
            self.ES=1
            pois = self.generatePoisson(TS)
            self.HS=self.TR + pois
        
        else:
            self.TF = self.TF+1
        
        exp = int(self.generateExponential(TEC))
        self.HC = self.TR + exp

    def processExit(self, TS):
        self.TR = self.HS
        if self.TF>0:
            self.TF=self.TF-1
            pois = self.generatePoisson(TS)
            self.HS = self.TR + pois
        else:
            self.ES=0
            self.HS = 9999 
            #TODO Generate output value

    def calculateStatistics(self):
        return

    def updateStatistics(self):
        data_aux = [self.TR, self.ES, self.TF, self.HS]
        self.data.append(data_aux)
        print(tabulate(self.data, headers=["TR", "ES", "TF", "HS"]))
        return
        

    def generateExponential(self, TEC):
        e = int(np.random.exponential(scale=TEC, size=None))
        return e

    def generatePoisson(self, TS):
        e = int(np.random.poisson(lam=TS, size=None))
        #print('valor de e', e)
        return e

    def __init__(self):
        TEC = int(input('Digite os valores para TEC: '))
        TS = int(input('Digite os valores para TS: '))
        time = int(input('Digite o tempo de execução: '))

        while time>self.TR:
            if self.HC < self.HS:
                self.processArrival(TEC, TS)
            else:
                self.processExit(7)
            self.updateStatistics()

        #TODO: Call function calculateStatistics()
    
class Random_Simulation:
    TR=0
    ES=0
    TF=0
    HC=0
    HS=9999

    data=[[]]

    def processArrival(self):
        self.TR=self.HC
        if self.ES==0 :
            self.ES=1
            ts_values = self.MMC_TS()
            self.HS=self.TR + ts_values
        
        else:
            self.TF = self.TF+1
        
        tec_values = int(self.MMC_TEC())
        self.HC = self.TR + tec_values
    

    def processExit(self):
        self.TR = self.HS
        if self.TF>0:
            self.TF=self.TF-1
            ts_values = self.MMC_TS()
            self.HS = self.TR + ts_values
        else:
            self.ES=0
            self.HS = 9999 
            #TODO Generate output value
    
    def MMC_TEC(self):
        lista = []
        for i in range(0,100):
            var = random.uniform(0, 1)
            lista.append(var)
        return sum(lista)/len(lista)

    def MMC_TS(self):
        lista = []
        for i in range(0,100):
            var = random.uniform(0, 1)
            lista.append(var)
        return sum(lista)/len(lista)
    
    def calculateStatistics(self):
        return

    def updateStatistics(self):
        data_aux = [self.TR, self.ES, self.TF, self.HS]
        self.data.append(data_aux)
        print(tabulate(self.data, headers=["TR", "ES", "TF", "HS"]))
        return
    
    def __init__(self):
        time = int(input('Digite o tempo de execução: '))

        while time>self.TR:
            if self.HC < self.HS:
                self.processArrival()
            else:
                self.processExit(7)
            self.updateStatistics()

        #TODO: Call function calculateStatistics()


if  __name__ == "__main__":
    
    menu()
    option = int(input())

    if(option == 1):
        S = Deterministic_Simulation()
    else:
        S = Random_Simulation()



    