import random
tam, prom = 0, 0
vec=[]
suma = 0
while tam<10 or tam>25:
    tam = int(round(random.random()*100))
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
for i in range (len(vec)):
    suma+=vec[i]
prom = suma // tam
print ("la suma de todos da: ",suma,"y el promedio es: ",prom)