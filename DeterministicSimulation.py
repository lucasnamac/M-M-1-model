import numpy as np
import time
from Queue import Queue
from functions import functions

class Deterministic_Simulation_lucas(functions):
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
    '''
    def calculateLambda(self, time):
        count=0
        lambd=0

        for i in self.TR_list:
            count+=1
            if i % 60 ==0:
                lambd+=count
            count=0

        lambd = lambd/(time/60)
        lambd = 60/int(lambd)    

        return lambd 

    def calculateMI(self, time):
        count=0
        mi=0

        for i in self.TR_list:
            count+=1
            if i % 60 ==0:
                mi+=count
            count=0

        mi = mi - self.TF_list[-1]
        mi = mi/(time/60)
        mi = 60/int(mi)
            #print(mi)
        return mi
    '''
    
    def calculateLambda2(self, time, clientes):
        lambd = clientes/(time/60)
        return lambd
    
    def calculateMI2(self, time):
        mi=0

        for i in self.TF_list:
            if i ==0:
                mi+=1

        return mi/(time/60)
    



    def updateStatistics(self, status, client):   
        print("Evento: " f"{status}  ", "Cliente: " f"{client}\t", "TR:" f"{self.TR}\t", "ES:" f"{self.ES}\t", "TF: "f"{self.TF}\t", "HS: "f"{self.HS}\t")
        self.TF_list.append(self.TF)
        self.ES_list.append(self.ES)
        self.TR_list.append(self.TR)
        time.sleep(0.2)
    
        

    def generateExponential(self, TEC):
        e = int(np.random.exponential(scale=TEC, size=None))
        return e

    def generatePoisson(self, TS):
        e = int(np.random.poisson(lam=TS, size=None))
        return e

    def __init__(self):
        QClient = []
        client =0
        TEC = int(input('Digite os valores para TEC: '))
        TS = int(input('Digite os valores para TS: '))
        time = int(input('Digite o tempo de execução: '))
        c = 0
        
        while time>self.TR:
            
            if self.HC < self.HS:
                self.processArrival(TEC, TS)
                status = "C"
                client += 1
                QClient.append(client)
                self.updateStatistics(status, client)
                
            else:
                self.processExit(TS)
                c = QClient.pop()
                status = "S"
                self.updateStatistics(status, c)
                
            

        mi = self.calculateMI2(time)
        lambd = self.calculateLambda2(time, client)
        #print("LAMBIDA EH {}   MI EH {}".format(lambd,mi))
        print("Numero medio de entidades na fila: ",super().calculo_LQ(lambd, mi))
        print("Taxa media de ocupação dos servidores: ",super().calculo_LS(lambd, mi))
        #print("Tempo medio de uma entidade na fila: {:.2f}",super().calculo_LS(lambd, mi))
        print("Tempo medio no sistema: ", super().calculo_W(lambd, mi))

        '''
        clientes_hora = client/(time/60) #Lambida
        #atendimento_clientes_hora =
        self.calculateMI() #Mi
        #print("Numero medio de entidades na fila", calculo_LQ(clientes_hora, atendimento_clientes_hora))
        #print("Tempo medio no sistema", calculo_W(clientes_hora, atendimento_clientes_hora))
        '''