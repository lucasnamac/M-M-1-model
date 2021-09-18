from math import e
import numpy as np
from numpy.random.mtrand import poisson
from tabulate import tabulate


class Simulation:
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

    def calculateStatistics(self):
        return



    #NOTE: Os valores não estão alinhados com a tabela. Ajuda nois rsrsrs
    def updateStatistics(self):   
        print("\t", "\t", self.TR, self.ES, self.TF, self.HS)
        

    
    

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


        print("Evento\t", "Cliente\t", "TR\t", "ES\t", "TF\t", "HS\t")
        while time>self.TR:
            if self.HC < self.HS:
                self.processArrival(TEC, TS)
            else:
                self.processExit(7)
            self.updateStatistics()

        #TODO: Call function calculateStatistics()


if  __name__ == "__main__":
    S = Simulation()