import random
from time import sleep
import numpy as np

def menu():
    print("\n1: Tempo medio de espera na fila: ")
    print("2: Probabilidade de um cliente esperar na fila:")
    print("3: Probabilidade do operador estar livre:")
    print("0: Sair\n")

def Tec(cliente):
    print("Determinar tempo entre chegadas (TEC):")
    tecList = []
    
    for i in range(0,cliente):
        tec = int(input("Entre com o TEC do {}º cliente: ".format(i+1)))
        tecList.append(tec)

    return tecList

def TS(cliente):
    print("Determinar tempo de serviço (TS):")
    tsList = []
    
    for i in range(0,cliente):
        ts = int(input("Entre com o TS do {}º cliente: ".format(i+1)))
        tsList.append(ts)

    return tsList




def Calculo_Chegada_Relogio(lista):
    tempo_chegada_relogio = []
    tempo_chegada_relogio.append(lista[0])
    for i in range(1,len(lista)):
        tempo_chegada_relogio.append(tempo_chegada_relogio[i-1] + lista[i])
    return tempo_chegada_relogio


def Calculo_Tempo_Servico(tempo_chegada, tempo_serviço, tempo_na_fila, cliente):
    inicio_service = []
    inicio_service.append(tempo_chegada[0])
    tempo_na_fila.append(0)

    if (tempo_chegada[0] + tempo_serviço[0] <= tempo_chegada[1]):
        inicio_service.append(tempo_chegada[1])
        tempo_na_fila.append(0)
    else:
        inicio_service.append(tempo_chegada[0] + tempo_serviço[0])
        tempo_na_fila.append(inicio_service[1] - tempo_chegada[1])


    for i in range(2,cliente):
        if (tempo_chegada[i-1] + tempo_serviço[i-1] <= tempo_chegada[i]):
            inicio_service.append(tempo_chegada[i])
            tempo_na_fila.append(0)
        else:
            inicio_service.append(tempo_chegada[i-1] + tempo_serviço[i-1])
            tempo_na_fila.append(inicio_service[i] - tempo_chegada[i])
    
    return inicio_service

def Calculo_Tempo_Final_Servico(valores_ts, inicio_servico_relogio,cliente):
    tempo_final_servico_relogio = []
    for i in range(0,cliente):
        tempo_final_servico_relogio.append(valores_ts[i] + inicio_servico_relogio[i])
    return tempo_final_servico_relogio

def Calculo_Tempo_Cliente_Sistema(valores_ts,tempo_na_fila,cliente):
    tempo_cliente_sistema = []
    for i in range(0,cliente):
        tempo_cliente_sistema.append(valores_ts[i] + tempo_na_fila[i])
    return tempo_cliente_sistema

def Calculo_Tempo_Livre_Operador(tempo_chegada_relogio,tempo_serviço,cliente):
    tempo_livre_operador = []
    tempo_livre_operador.append(tempo_chegada_relogio[0])

    if (tempo_chegada_relogio[0] + tempo_serviço[0] <= tempo_chegada_relogio[1]):
        tempo_livre_operador.append(tempo_chegada_relogio[1] - tempo_chegada_relogio[0] - tempo_serviço[0])
    else:
        tempo_livre_operador.append(0)

    for i in range(2,cliente):
        if (tempo_chegada_relogio[i-1] + tempo_serviço[i-1] <= tempo_chegada_relogio[i]):
            tempo_livre_operador.append(tempo_chegada_relogio[i] - tempo_chegada_relogio[i-1] - tempo_serviço[i-1])
        else:
            tempo_livre_operador.append(0)
    return tempo_livre_operador

def print_table(lista):
    print(lista)
    return

def generate_matrix(cliente,valores_tec,valores_ts,tempo_chegada_relogio,inicio_servico_relogio,tempo_na_fila,tempo_final_servico_relogio,tempo_cliente_sistema,tempo_livre_operador):
    for i in range(0,cliente):
        if i >=9:
            print(i+1, "        ", valores_tec[i],"             ", tempo_chegada_relogio[i],"           ", valores_ts[i],"           ", inicio_servico_relogio[i],"             ", tempo_na_fila[i],"               ", tempo_final_servico_relogio[i],"               ", tempo_cliente_sistema[i],"               ", tempo_livre_operador[i])
        else:
            print(i+1, "         ", valores_tec[i],"             ", tempo_chegada_relogio[i],"           ", valores_ts[i],"           ", inicio_servico_relogio[i],"             ", tempo_na_fila[i],"               ", tempo_final_servico_relogio[i],"               ", tempo_cliente_sistema[i],"               ", tempo_livre_operador[i])

    return

def tamanho_fila(tempo_fila,cliente):
    qtd = 0
    for i in range(0,cliente):
        if tempo_fila[i] != 0:
            qtd += 1
    return qtd


        
   
def main():
    valores_tec = []
    valores_ts = []
    tempo_chegada_relogio = []
    inicio_servico_relogio = []
    tempo_na_fila = []
    tempo_final_servico_relogio = []
    tempo_cliente_sistema = []
    tempo_livre_operador = []
    qtd_fila = 0

    

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("SIMULAÇÃO DE SISTEMA M/M/1 DETERMINISTICO")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    cliente = 0
    while(cliente <2):
        cliente = int(input("Quantos clientes?(mínimo 2): "))
        if(cliente <2):
            print("Digite um valor maior ou igual a 2!")

    valores_tec = Tec(cliente)
    valores_ts = TS(cliente)
    tempo_chegada_relogio = Calculo_Chegada_Relogio(valores_tec)
    inicio_servico_relogio = Calculo_Tempo_Servico(tempo_chegada_relogio, valores_ts, tempo_na_fila,cliente)
    tempo_final_servico_relogio = Calculo_Tempo_Final_Servico(valores_ts,inicio_servico_relogio,cliente)
    tempo_cliente_sistema = Calculo_Tempo_Cliente_Sistema(valores_ts,tempo_na_fila,cliente)
    tempo_livre_operador = Calculo_Tempo_Livre_Operador(tempo_chegada_relogio,valores_ts,cliente)
    qtd_fila = tamanho_fila(tempo_na_fila,cliente)

    print("\nCliente     TEC       T.Chegada.Relogio     TS      T.Ini.Serv.Relo     T.Cli.Fila     T.Final.Serv.Relo      T.Cli.Sis          T.Livre.OP")
    
    
    generate_matrix(cliente,valores_tec,valores_ts,tempo_chegada_relogio,inicio_servico_relogio,tempo_na_fila,tempo_final_servico_relogio,tempo_cliente_sistema,tempo_livre_operador)

    
    print("\nOPÇÕES: ")
    option = -1
    while(option != 0):
        menu()
        option = int(input("Digite uma opcao: "))
        if(option == 1):
            print(sum(tempo_na_fila)/15)
        elif(option == 2):
            print(qtd_fila/15)
        elif(option == 3):
            print(sum(tempo_livre_operador)/tempo_final_servico_relogio[14])
        elif (option == 0):
            print("Até breve!")
            sleep(1)
            exit(1)
        else:
            print("Digite uma opcao válida!")
        


if __name__ == "__main__":
    main()