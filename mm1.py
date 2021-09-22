import random
from time import process_time_ns
import functions
import numpy as np

def menu():
    print("\n1: Numero medio de clientes na fila esperando atendimento")
    print("2: Tempo medio gasto por um cliente no sistema")
    print("3: Numero de clientes atendidos por hora")
    print("4: Probabilidade de se ter X clientes no sistema")
    print("0: Sair\n")

def Tec():
    print("Determinar tempo entre chegadas (TEC):")
    tecList = []
    listaTecs = []
    
    for i in range(0,3):
        tec = int(input("Entre com o {}º TEC (tempo entre chegadas de clientes) em minutos: ".format(i+1)))
        tecList.append(tec)
    for j in range(0,15):
        x = random.choice(tecList)
        listaTecs.append(x)
    return listaTecs

def TS():
    print("Determinar tempo de serviço (TS):")
    tsList = []
    listaTs = []
    
    for i in range(0,3):
        ts = int(input("Entre com o {}º TS (tempo de serviço) em minutos: ".format(i+1)))
        tsList.append(ts)
    for j in range(0,15):
        x = random.choice(tsList)
        listaTs.append(x)
    return listaTs




def Calculo_Chegada_Relogio(lista):
    tempo_chegada_relogio = []
    tempo_chegada_relogio.append(lista[0])
    for i in range(1,len(lista)):
        tempo_chegada_relogio.append(tempo_chegada_relogio[i-1] + lista[i])
    return tempo_chegada_relogio


def Calculo_Tempo_Servico(tempo_chegada, tempo_serviço, tempo_na_fila):
    inicio_service = []
    inicio_service.append(tempo_chegada[0])
    tempo_na_fila.append(0)

    if (tempo_chegada[0] + tempo_serviço[0] <= tempo_chegada[1]):
        inicio_service.append(tempo_chegada[1])
        tempo_na_fila.append(0)
    else:
        inicio_service.append(tempo_chegada[0] + tempo_serviço[0])
        tempo_na_fila.append(inicio_service[1] - tempo_chegada[1])


    for i in range(2,15):
        if (tempo_chegada[i-1] + tempo_serviço[i-1] <= tempo_chegada[i]):
            inicio_service.append(tempo_chegada[i])
            tempo_na_fila.append(0)
        else:
            inicio_service.append(tempo_chegada[i-1] + tempo_serviço[i-1])
            tempo_na_fila.append(inicio_service[i] - tempo_chegada[i])
    
    return inicio_service

def Calculo_Tempo_Final_Servico(tempo_chegada_relogio, inicio_servico_relogio,tempo_na_fila):
    tempo_final_servico_relogio = []
    for i in range(0,15):
        tempo_final_servico_relogio.append(tempo_chegada_relogio[i] + inicio_servico_relogio[i] + tempo_na_fila[i])
    return tempo_final_servico_relogio

def Calculo_Tempo_Cliente_Sistema(valores_ts,tempo_na_fila):
    tempo_cliente_sistema = []
    for i in range(0,15):
        tempo_cliente_sistema.append(valores_ts[i] + tempo_na_fila[i])
    return tempo_cliente_sistema

def Calculo_Tempo_Livre_Operador(tempo_chegada_relogio,tempo_serviço):
    tempo_livre_operador = []
    tempo_livre_operador.append(tempo_chegada_relogio[0])

    if (tempo_chegada_relogio[0] + tempo_serviço[0] <= tempo_chegada_relogio[1]):
        tempo_livre_operador.append(tempo_chegada_relogio[1] - tempo_chegada_relogio[0] - tempo_serviço[0])
    else:
        tempo_livre_operador.append(0)

    for i in range(2,15):
        if (tempo_chegada_relogio[i-1] + tempo_serviço[i-1] <= tempo_chegada_relogio[i]):
            tempo_livre_operador.append(tempo_chegada_relogio[i] - tempo_chegada_relogio[i-1] - tempo_serviço[i-1])
        else:
            tempo_livre_operador.append(0)
    return tempo_livre_operador

def print_table(lista):
    print(lista)
    return

def generate_matrix(cliente,valores_tec,valores_ts,tempo_chegada_relogio,inicio_servico_relogio,tempo_na_fila,tempo_final_servico_relogio,tempo_cliente_sistema,tempo_livre_operador):
    for i in range(0,15):
        if i >=9:
            print(" ",cliente[i],"        ", valores_tec[i],"             ", tempo_chegada_relogio[i],"           ", valores_ts[i],"           ", inicio_servico_relogio[i],"             ", tempo_na_fila[i],"               ", tempo_final_servico_relogio[i],"               ", tempo_cliente_sistema[i],"               ", tempo_livre_operador[i])
        else:
            print(" ",cliente[i],"         ", valores_tec[i],"             ", tempo_chegada_relogio[i],"           ", valores_ts[i],"           ", inicio_servico_relogio[i],"             ", tempo_na_fila[i],"               ", tempo_final_servico_relogio[i],"               ", tempo_cliente_sistema[i],"               ", tempo_livre_operador[i])

    return

def tamanho_fila(tempo_fila):
    qtd = 0
    for i in range(0,15):
        if tempo_fila[i] != 0:
            qtd += 1
    return qtd

def calculo_lambida(valores_tec):
    aux = sum(valores_tec)/15
    lambida = 60/aux
    print("Lambida eh: ",lambida)
    return lambida

def calculo_mi(valores_ts):
    aux = sum(valores_ts)/15
    mi = 60/aux
    print("MI eh: ",mi)
    return mi

            

   
def main():
    cliente = []
    valores_tec = []
    valores_ts = []
    tempo_chegada_relogio = []
    inicio_servico_relogio = []
    tempo_na_fila = []
    tempo_final_servico_relogio = []
    tempo_cliente_sistema = []
    tempo_livre_operador = []
    qtd_fila = 0

    for i in range(1,16):
        cliente.append(i)

    
    

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("SIMULAÇÃO DE SISTEMA M/M/1 DETERMINISTICO")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    valores_tec = Tec()
    valores_ts = TS()
    tempo_chegada_relogio = Calculo_Chegada_Relogio(valores_tec)
    inicio_servico_relogio = Calculo_Tempo_Servico(tempo_chegada_relogio, valores_ts, tempo_na_fila)
    tempo_final_servico_relogio = Calculo_Tempo_Final_Servico(tempo_chegada_relogio,inicio_servico_relogio,tempo_na_fila )
    tempo_cliente_sistema = Calculo_Tempo_Cliente_Sistema(valores_ts,tempo_na_fila)
    tempo_livre_operador = Calculo_Tempo_Livre_Operador(tempo_chegada_relogio,valores_ts)
    qtd_fila = tamanho_fila(tempo_na_fila)

    print("Cliente     TEC       T.Chegada.Relogio    TS       T.Ini.Serv.Relo     T.Cli.Fila     T.Final.Serv.Relo    T.Cli.Sis        T.Livre.OP")
    
    
    generate_matrix(cliente,valores_tec,valores_ts,tempo_chegada_relogio,inicio_servico_relogio,tempo_na_fila,tempo_final_servico_relogio,tempo_cliente_sistema,tempo_livre_operador)

    print("\n Tempo medio de espera na fila: ",sum(tempo_na_fila)/15)
    print("\n Probabilidade de um cliente esperar na fila: ",qtd_fila/15)
    print("\n Probabilidade do operador estar livre: ",sum(tempo_livre_operador)/tempo_final_servico_relogio[14])
    
    lambida = calculo_lambida(valores_tec)
    mi = calculo_mi(valores_ts)


    
    print("OPÇÕES: ")
    option = -1
    while(option != 0):
        menu()
        option = int(input("Digite uma opcao: "))
        if(option == 1):
            print(functions.calculo_LQ(lambida, mi))
        elif(option == 2):
            print(functions.calculo_W(lambida, mi))
        elif(option == 3):
            print((lambida/mi)*mi)
        elif(option == 4):
            clientes_no_sistema = int(input("Entre com o valor de X: "))
            print("A probabilidade de se ter {} no sistema eh: {}".format(clientes_no_sistema, functions.calculo_pi(lambida, mi, clientes_no_sistema)))
        else:
            print("Digite uma opcao válida!")
        


if __name__ == "__main__":
    main()
lista = []
for i in range(0,100):
    var = random.uniform(0, 1)
    lista.append(var)
print(sum(lista)/len(lista))