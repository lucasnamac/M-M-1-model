import random
lista = []
for i in range(0,100):
    var = random.uniform(0, 1)
    lista.append(var)
print(sum(lista)/len(lista))