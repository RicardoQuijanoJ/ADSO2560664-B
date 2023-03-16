import random
tam=1
while tam<10 or tam>25:
    tam=round(random.random()*100)
print(tam)

lista1=[]
suma=0
prom=0
for i in range (tam):
    lista1.insert(i,round(random.random()*100))
    