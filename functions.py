
class functions():

    def calculo_L(self,lambida, mi):
        #Media do numero de clientes presentes em todo o sistema
        l = (lambida / (lambida/mi))
        return l

    def calculo_LQ(self,lambida, mi):
        #Numero medio de clientes na fila esperando atendimento
        lq = ((lambida/mi) * (lambida/mi)) / (1-(lambida/mi))
        return lq

    def calculo_LS(self,lambida, mi):
        #Numero medio de clientes em atendimento
        ls = (lambida/mi)
        return ls

    def calculo_W(self,lambida, mi):
        #Tempo medio gasto por um cliente no sistema
        l = self.calculo_L(lambida, mi)
        w = l / lambida
        return w

    def calculo_pi(self,lambida, mi, clientes_no_sistema):
        #Probabilidade de X clientes no sistema em determinado momento
        p = (lambida/mi)
        if (clientes_no_sistema == 0):
            return (1 - p)
        else:
            return ((p ** clientes_no_sistema) * (1-p))

