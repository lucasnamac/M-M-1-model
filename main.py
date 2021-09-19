from math import e
import numpy as np
from numpy.random.mtrand import poisson
import time
import random


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
    print("2: Random Simulation")
    return

class Deterministic_Simulation:
    TR=0
    ES=0
    TF=0
    HC=0
    HS=9999

    TF_list = []
    ES_list = []
    TR_list = []

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

    def calculateMI(self, time):
        aux = 0
        for j in self.TF_list:
            if(j == 0):
                aux += 1
        return aux/(time/60)


    def updateStatistics(self, status, client):   
        print("Evento: " f"{status}  ", "Cliente: " f"{client}\t", "TR:" f"{self.TR}\t", "ES:" f"{self.ES}\t", "TF: "f"{self.TF}\t", "HS: "f"{self.HS}\t")
        self.TF_list.append(self.TF)
        self.ES_list.append(self.ES)
        self.TR_list.append(self.TR)
        time.sleep(0.5)
        

    def generateExponential(self, TEC):
        e = int(np.random.exponential(scale=TEC, size=None))
        return e

    def generatePoisson(self, TS):
        e = int(np.random.poisson(lam=TS, size=None))
        return e

    def __init__(self):
        client=0
        TEC = int(input('Digite os valores para TEC: '))
        TS = int(input('Digite os valores para TS: '))
        time = int(input('Digite o tempo de execução: '))

        
        while time>self.TR:
            client+=1
            if self.HC < self.HS:
                self.processArrival(TEC, TS)
                status = "C"
            else:
                self.processExit(TS)
                status = "S"
            self.updateStatistics(status, client)

        clientes_hora = client/(time/60) #Lambida
        atendimento_clientes_hora = self.calculateMI(time) #Mi
        print("Numero medio de entidades na fila", calculo_LQ(clientes_hora, atendimento_clientes_hora))
        print("Tempo medio no sistema", calculo_W(clientes_hora, atendimento_clientes_hora))


class Random_Simulation:
    TR=0
    ES=0
    TF=0
    HC=0
    HS=9999

    TF_list = []
    ES_list = []

    def processArrival(self):
        self.TR=self.HC
        if self.ES==0 :
            self.ES=1
            ts_values = int(self.MMC_TS())
            self.HS=self.TR + ts_values     
        else:
            self.TF = self.TF+1
        
        tec_values = int(self.MMC_TEC())
        self.HC = self.TR + tec_values
    

    def processExit(self):
        self.TR = self.HS
        if self.TF>0:
            self.TF=self.TF-1
            ts_values = int(self.MMC_TS())
            self.HS = self.TR + ts_values
        else:
            self.ES=0
            self.HS = 9999 
    
    def MMC_TEC(self):
        lista = []
        for i in range(0,100):
            var = random.uniform(0, 1)
            lista.append(var)
        return (sum(lista)/len(lista)) * 10

    def MMC_TS(self):
        lista = []
        for i in range(0,100):
            var = random.uniform(0, 1)
            lista.append(var)
        return (sum(lista)/len(lista)) * 10
    
    def calculateStatistics(self):
        return

    
    def updateStatistics(self, status, client):   
        print("Evento: " f"{status}  ", "Cliente: " f"{client}\t", "TR:" f"{self.TR}\t", "ES:" f"{self.ES}\t", "TF: "f"{self.TF}\t", "HS: "f"{self.HS}\t")
        self.TF_list.append(self.TF)
        self.ES_list.append(self.ES)
        time.sleep(0.5)
    
    def __init__(self):
        client=0
        time = int(input('Digite o tempo de execução: '))
   
        while time>self.TR:
            client+=1
            if self.HC < self.HS:
                self.processArrival()
                status = "C"
            else:
                self.processExit()
                status = "S"
            self.updateStatistics(status, client)

if  __name__ == "__main__":
    
    menu()
    option = int(input())

    if(option == 1):
        S = Deterministic_Simulation()
    else:
        S = Random_Simulation()






    







    