import random
import numpy
def randomPerm(n):
    v=[]
    for i in range(n):
        v.append(i+1)
    for i in range(len(v)-1):
        j = random.randint(i, len(v)-1)
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
    return v
def insertionSort3(lista):
    retorno = lista
    pasos = 1
    for i in range(1,len(retorno)):
        pasos = pasos+2
        ValorC = retorno[i]
        pasos = pasos+1
        posicion = i
        pasos = pasos+2
        while posicion>0 and retorno[posicion-1]>ValorC:
            retorno[posicion]=retorno[posicion-1]
            pasos = pasos+1
            posicion = posicion-1
            pasos = pasos+1
            retorno[posicion]=ValorC
            pasos = pasos+1
    return pasos
##################################
def insertionSort4(lista): # numero de intercambios
    retorno = lista
    pasos = 0
    for i in range(1,len(retorno)):
        ValorC = retorno[i]
        pasos = pasos+1
        posicion = i
        while posicion>0 and retorno[posicion-1]>ValorC:
            retorno[posicion]=retorno[posicion-1]
            pasos = pasos+1
            posicion = posicion-1
            retorno[posicion]=ValorC
            pasos = pasos+1
    return pasos
############################################
def insertionSort5(lista): # numero de preguntas en el while
    retorno = lista
    pasos = 0
    for i in range(1,len(retorno)):
        ValorC = retorno[i]
        posicion = i
        while posicion>0 and retorno[posicion-1]>ValorC:
            pasos = pasos+1
            retorno[posicion]=retorno[posicion-1]
            posicion = posicion-1
            retorno[posicion]=ValorC
    return pasos
###################################################
def insertionSort6(lista): # numero de comparaciones
    retorno = lista
    pasos = 0
    for i in range(1,len(retorno)):
        pasos = pasos+1
        ValorC = retorno[i]
        posicion = i
        while posicion>0 and retorno[posicion-1]>ValorC:
            pasos = pasos+1
            retorno[posicion]=retorno[posicion-1]
            posicion = posicion-1
            retorno[posicion]=ValorC
    return pasos
############################################
n = 4
runs = 200

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
min1 = n**3
max1 = 0
min2 = n**3
max2 = 0
min3 = n**3
max3 = 0
min4 = n**3
max4 = 0
for i in range(runs):
    t1 = insertionSort3(randomPerm(n))
    t2 = insertionSort4(randomPerm(n))
    t3 = insertionSort5(randomPerm(n))
    t4 = insertionSort6(randomPerm(n))
    if t1 < min1 :
       min1 = t1
    if t1 > max1 :
       max1 = t1
    if t2 < min2 :
       min2 = t2
    if t2 > max2 :
       max2 = t2
    if t3 < min3 :
       min3 = t3
    if t3 > max3 :
       max3 = t3
    if t4 < min4 :
       min4 = t4
    if t4 > max4 :
       max4 = t4
    sum1 = sum1 + t1
    sum2 = sum2 + t2
    sum3 = sum3 + t3
    sum4 = sum4 + t4

print 'menor numero de pasos ' + str(min1)
print 'mayor numero de pasos ' + str(max1)
print 'promedio de pasos ' + str(sum1/runs)
print("###################################")
print 'menor numero de preguntas ' + str(min2)
print 'mayor numero de preguntas ' + str(max2)
print 'promedio de preguntas ' + str(sum2/runs)
print("###################################")
print 'menor numero de swaps ' + str(min3)
print 'mayor numero de swaps ' + str(max3)
print 'promedio de swaps ' + str(sum3/runs)
print("###################################")
print 'menor numero de preguntas en el while ' + str(min4)
print 'mayor numero de preguntas en el while ' + str(max4)
print 'promedio de preguntas en el while ' + str(sum4/runs)
