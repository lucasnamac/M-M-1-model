from math import e
import numpy as np


class Simulation:
    TR=0
    ES=0
    TF=0
    HC=0
    HS=9999

    def processArrival(self, TEC, TS):
        self.TR=self.HC

        if self.ES==0 :
            self.ES=1
            #TODO: Generate service time
            self.HS=self.TR+ TS
        
        else:
            self.TF = self.TF+1
        
        #TODO: Generate lenght for next arrival  - TEC
        self.HC = self.TR + TEC

    def processExit(self, TS):
        self.TR = self.HS
        if self.TF>0:
            self.TF=self.TF-1
            #TODO: Generate service time
            self.HS = self.TR + TS
        else:
            ES=0
            #TODO Generate output value

    def calculateStatistics(self):
        return

    def updateStatistics(self):
        return

    def generateExponential(self):
        e = np.random.exponential(scale=10, size=None)
        print(e)

    def __init__(self):
        time = 5
        while time< self.TR:
            if self.HC < self.HS:
                self.processArrival(4, 7)
            else:
                self.processExit(7)
            
            # TODO: Call function updateStatistics()

        #TODO: Call function calculateStatistics()


if  __name__ == "__main__":
    S = Simulation()
    S.generateExponential() 