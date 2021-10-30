import random
import numpy as np
import time
import tabulate
import math

class RandomSimulationMM2():
    NClients = 0
    TEC = 0
    TS = 0
    time = 0
    TR=0
    ES1=0
    ES2=0
    TF=0
    HC=0
    HS=9999
    nServer=0

    arrive = []
    TF_list = []
    ES_list= []
    nServer_list = []
    TR_list = []
    TM_list = []
    HS_list = []
    data = []

    def menu(self):
        self.time = int(input('Digite o tempo de execução: '))
        self.TEC = self.TECGenerate()
        self.TS = self.TSGenerate()
        return


    def TECGenerate(self):
        options = []
        TEC = 0
        aux = 0
        print("\nEscolha uma distribuição para TEC")
        print("1- Distribuição Normal")
        print("2- Distribuição Exponencial")
        print("3- Distribuição Poisson")
        distributionType = int(input())
        lamb = int(input("Entre com o valor de lambida: "))
        if distributionType == 1:  
            for i in range(0,100):
                aux = np.random.normal(0, lamb)
                if aux < 0:
                    aux = aux * -1
                if aux >1:
                    aux = aux/10
                options.append(aux)

        if distributionType == 2:  
            for i in range(0,100):
                aux = np.random.exponential(lamb)
                if aux < 0:
                    aux = aux * -1
                if aux >1:
                    aux = aux/10
                options.append(aux)
        
        if distributionType == 3:  
            for i in range(0,100):
                aux = np.random.poisson(lam=lamb)
                aux = aux/10
                options.append(aux)

        k = 1 + 3.3*math.log10(100) #7.6 aprox 8
        h = max(options)*100/ k

        value = random.choice(options)*100
        if value >= 0.0 and value <= h: #Classe0_8
            TEC = (0 + h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= h and value < 2*h: #Classe8_16
            TEC = (h + 2*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 2*h and value < 3*h: #Classe16_24
            TEC = (2*h + 3*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 3*h and value < 4*h: #Classe24_32
            TEC = (3*h+ 4*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 4*h and value < 5*h: #Classe32_40
            TEC = (4*h+ 5*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 5*h and value < 6*h: #Classe40_48
            TEC = (5*h+ 6*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 6*h and value < 7*h: #Classe48_56
            TEC = (6*h+ 7*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
        elif value >= 7*h and value < 8*h: #Classe56_64
            TEC = (7*h+ 8*h)/2
            print("O valor de TEC é: ",int(TEC))
            return int(TEC)
    
    def TSGenerate(self):
        options = []
        TS = 0
        print("\nEscolha uma distribuição para TS")
        print("1- Distribuição Normal")
        print("2- Distribuição Exponencial")
        print("3- Distribuição Poisson")

        distributionType = int(input())
        lamb = int(input("Entre com o valor de lambida: "))
        if distributionType == 1:  
            for i in range(0,100):
                aux = np.random.normal(0, lamb)
                if aux < 0:
                    aux = aux * -1
                if aux >1:
                    aux = aux/10
                options.append(aux)

        if distributionType == 2:  
            for i in range(0,100):
                aux = np.random.exponential(lamb)
                if aux < 0:
                    aux = aux * -1
                if aux >1:
                    aux = aux/10
                options.append(aux)
        
        if distributionType == 3:  
            for i in range(0,100):
                aux = np.random.poisson(lam=lamb)
                aux = aux/10
                options.append(aux)

        k = 1 + 3.3*math.log10(100) #7.6 aprox 8
        h = max(options)*100/ k
        
        value = random.choice(options)*100

        if value >= 0.0 and value <= h: #Classe0_8
            TS = (0 + h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= h and value < 2*h: #Classe8_16
            TS = (h + 2*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 2*h and value < 3*h: #Classe16_24
            TS = (2*h + 3*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 3*h and value < 4*h: #Classe24_32
            TS = (3*h+ 4*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 4*h and value < 5*h: #Classe32_40
            TS = (4*h+ 5*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 5*h and value < 6*h: #Classe40_48
            TS = (5*h+ 6*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 6*h and value < 7*h: #Classe48_56
            TS = (6*h+ 7*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)
        elif value >= 7*h and value < 8*h: #Classe56_64
            TS = (7*h+ 8*h)/2
            print("O valor de TS é: ",int(TS))
            time.sleep(1.5)
            return int(TS)

            

    def processArrival(self, TEC, TS):
        self.TR=self.HC

        if self.ES1==0:
            self.ES1=1
            self.HS=self.TR + TS
            self.nServer=1
        
        elif self.ES2==0:
            self.ES2=1
            self.HS=self.TR + TS
            self.nServer =2

        elif self.ES1!=0 or self.ES2!=0:
            self.TF = self.TF+1
            
        self.HC = self.TR + TEC
    
    def processArrivalLimit(self, TEC, TS, limit):
        nServer=0
        self.TR=self.HC
        if self.ES1==0:
            self.ES1=1
            self.HS=self.TR + TS
            nServer=1
        
        elif self.ES2==0:
            self.ES2=1
            self.HS=self.TR + TS
            nServer=2
        else:
            if(self.TF < limit):
                self.TF = self.TF+1
        
        self.HC = self.TR + TEC
        return nServer

    def processExit(self, TS):
        self.TR = self.HS
        if self.TF>0:
            self.TF=self.TF-1
            self.HS = self.TR + TS
        else:
            self.ES2=0
            self.ES1=0
            self.HS = 9999



    def updateStatistics(self, status, client):
        self.TF_list.append(self.TF)
        self.TR_list.append(self.TR)
        self.HS_list.append(self.HS - self.TR)
        self.nServer_list.append(self.nServer)

        #if self.nServer == 1:
        self.ES_list.append(self.ES1)
        self.data.append([status, client, self.TR, self.nServer,self.ES1, self.TF, self.HC, self.HS])
        #if self.nServer ==2:
        #    self.data.append([status, client, self.TR, nServer,self.ES2, self.TF, self.HC, self.HS])
        self.ES_list.append(self.ES2)

        if status == "Chegada":
            self.arrive.append([status, client, self.TR, self.TF, self.HC, self.HS])

        if self.TF > 0:
            self.TM_list.append(self.HS - self.TR)
        return
    
    def process_with_queue_limit(self):
        QClient = []
        client =0
        self.menu()
        limit = int(input("Digite o tamanho da fila: "))
        
        while self.time>self.TR:
            
            if self.HC < self.HS:
                self.processArrivalLimit(self.TEC, self.TS, limit)
                status = "Chegada"
                client += 1
                self.NClients +=1
                QClient.append(client)
                self.updateStatistics(status, client)
                
                
            else:
                self.processExit(self.TS)
                c = QClient.pop()
                status = "Saída"
                self.updateStatistics(status, c)
                
    
    def process_without_queue_limit(self):
        QClient = []
        client =0
        self.menu()
        
        while self.time>self.TR:
            print("valor de hc", self.HC)
            print("valor de HS", self.HS)

            
            if self.HC < self.HS:
                self.processArrival(self.TEC, self.TS)
                status = "Chegada"
                client += 1
                self.NClients +=1
                QClient.append(client)
                self.updateStatistics(status, client)
                
            else:
                self.processExit(self.TS)
                c = QClient.pop()
                status = "Saída"
                self.updateStatistics(status, c)
    
    def calculateStatistics(self):
        print("Número medio de entidades na fila: ", sum(self.TF_list)/len(self.TF_list))
        print("Taxa medio de ocupação do servidor: ", sum(self.ES_list)/len(self.data))
        print("Tempo medio de uma entidade na fila: ", sum(self.TM_list)/len(self.arrive))
        print("Tempo medio no sistema: ", self.TR_list[-1]/len(self.arrive))
        
        
 

    def __init__(self, option2):
        self.option2 = option2

        if(option2 == 1):
            self.process_with_queue_limit()
        elif(option2 == 2):
            self.process_without_queue_limit()
    


        

    