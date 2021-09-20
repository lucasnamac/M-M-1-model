import numpy as np
import time
from Queue import Queue

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


    def calculate_LQ(self, lambida, mi):
        #Numero medio de clientes na fila esperando atendimento
        lq = ((lambida/mi) * (lambida/mi)) / (1-(lambida/mi))
        return lq
        

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
        QClient = Queue()
        client =0
        TEC = int(input('Digite os valores para TEC: '))
        TS = int(input('Digite os valores para TS: '))
        time = int(input('Digite o tempo de execução: '))

        
        while time>self.TR:
            
            if self.HC < self.HS:
                self.processArrival(TEC, TS)
                status = "C"
                client += 1
                QClient.enqueue(client)
                
            else:
                self.processExit(TS)
                client = QClient.dequeue()
                status = "S"
                
            self.updateStatistics(status, client)

        mi = self.calculateMI(time)
        lambd = self.calculateLambda(time)
        print("Numero medio de entidades na fila: {:.2f}".format( self.calculate_LQ(lambd, mi)))

        '''
        clientes_hora = client/(time/60) #Lambida
        #atendimento_clientes_hora =
        self.calculateMI() #Mi
        #print("Numero medio de entidades na fila", calculo_LQ(clientes_hora, atendimento_clientes_hora))
        #print("Tempo medio no sistema", calculo_W(clientes_hora, atendimento_clientes_hora))
        '''