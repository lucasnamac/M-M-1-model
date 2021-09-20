import numpy as np
import random
import time

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