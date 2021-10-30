import random
import numpy as np
import time
import tabulate
import math

class DeterministicSimulationMM2():
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
        self.TEC = int(input('Digite o valor para TEC: '))
        self.TS = int(input('Digite o valor para TS: '))
        self.time = int(input('Digite o tempo de execução: '))


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
    


        

    