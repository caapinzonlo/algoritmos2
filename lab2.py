import numpy as np
from matplotlib import pyplot as plt
import time
import itertools
import random
#########################################
#                                       #
#           funciones                   #
#########################################
def insertionSort2(lista):
    retorno = lista
    for i in range(1,len(retorno)):
        ValorC = retorno[i]
        posicion = i
        while posicion>0 and retorno[posicion-1]>ValorC:
            retorno[posicion]=retorno[posicion-1]
            posicion = posicion-1
            retorno[posicion]=ValorC
    return retorno
#############################################
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
###########################################
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
###########################################
def I_S_Total(n):
    my_list = []
    Vpasos = []
    for i in range(0,n):
        my_list.append(i)

    permutations = itertools.permutations(my_list,len(my_list))

    for i in permutations:
        salida = insertionSort3(list(i))
        Vpasos.append(salida)
    return Vpasos
##############################################
def I_S_Total2(n):
    my_list = []
    Vpasos = []
    for i in range(0,n):
        my_list.append(i)

    permutations = itertools.permutations(my_list,len(my_list))

    for i in permutations:
        salida = insertionSort4(list(i))
        Vpasos.append(salida)
    return Vpasos
##############################################
def I_S_Total3(n):
    my_list = []
    Vpasos = []
    for i in range(0,n):
        my_list.append(i)

    permutations = itertools.permutations(my_list,len(my_list))

    for i in permutations:
        salida = insertionSort5(list(i))
        Vpasos.append(salida)
    return Vpasos
##############################################
def I_S_Total4(n):
    my_list = []
    Vpasos = []
    for i in range(0,n):
        my_list.append(i)

    permutations = itertools.permutations(my_list,len(my_list))

    for i in permutations:
        salida = insertionSort6(list(i))
        Vpasos.append(salida)
    return Vpasos
##############################################
def Cpromedio(list):    # funcion para hallar el promedio de pasos
    tam = len(list)
    suma = 0
    for i in range(0,tam):
        suma = suma + list[i]
    promedio = suma/tam
    return promedio
########################################
def ordenPasos(list):       # funcion que saca el numero de pasos sin repetir en la lista
    comp = []
    comp.append(list[0])
    for i in range(1,len(list)):
        num = list[i]
        contador = 0
        for j in range(0,len(comp)):
            if comp[j]!=V[i]:
                contador = contador+1
        if contador==len(comp):
            comp.append(list[i])
    return comp
#########################################
#                                       #
#       Inicia el programa principal    #
#########################################
#                                       #
#       punto 1                         #
#########################################
s0 = 1
s1 =1
Y1 = []
Y2 = []
Y3 = []
X1 = []
cont = 0
for i in range(1,50000):      # En este for se realiza la sucesion de fibonachi
    a = time.clock() # se usa para medir el tiempo incial
    fibonachi = s0+s1
    s0=s1
    s1 = fibonachi
    Y1.append(fibonachi)
    X1.append(i)
    b = time.clock() # Se mide el tiempon final
    tiempo = b-a            #se obtiene el tiempo del proceso
    cont = cont+tiempo
    Y2.append(cont)
    Y3.append(tiempo)
print("Grafica de fibonachi en el tiempo")
plt.figure(1)       # se genera la grafica
plt.plot(X1,Y2)
plt.show()
plt.figure(2)       # se genera la grafica
plt.plot(X1,Y3)
plt.show()
##############################################
#Punto 2                                     #
# usando itertools                           #
##############################################
V=I_S_Total(4)
V2=I_S_Total2(4)
V3=I_S_Total3(4)
V4=I_S_Total4(4)
#print(V)
prom = Cpromedio(V)
#print(prom)
comp = ordenPasos(V)
######################
casos = []
casos2 = []
casos3 = []
casos4 = []
for i in range(0,len(comp)):
    contador_casos = 0
    for j in range(0,len(V)):
        if comp[i]==V[j]:
            contador_casos = contador_casos+1
    casos.append(contador_casos)
print("numero de instrucciones")
plt.figure(2)       # se genera la grafica
plt.plot(comp,casos)
plt.show()
plt.figure(3)
plt.hist(V,50,facecolor='g')
plt.show()
print("numero de swaps")
plt.figure(4)
plt.hist(V2,50,facecolor='g')
plt.show()
print("numero de preguntas en el whilE")
plt.figure(5)
plt.hist(V3,50,facecolor='g')
plt.show()
print("numero de preguntas")
plt.figure(6)
plt.hist(V4,50,facecolor='g')
plt.show()
print("promedio de instrucciones "+str(prom))
print("mejor de los casos "+str(V[0]))
print("peor de los casos "+str(V[-1]))
#################################################
#                                               #
#       Punto 2 con el codigo de daniel jimenez #
#################################################
print("Usando el código de daniel jimenez")
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
def permutaciones(n):
    k = []
    k.append(randomPerm(n))
    cont = 1
    cont2 = 0
    while cont<n:
        sm = randomPerm(n)
        for i in range(0,len(k)):
            if sm != len(k):
                cont2 = cont2+1
        if cont2 ==len(k):
            k.append(randomPerm(n))
            cont = cont+1

    print(k)
    return k
def I_S_Totalb(n):
    Vpasos = []
    permutations = permutaciones(n)
    for i in permutations:
        salida = insertionSort3(list(i))
        Vpasos.append(salida)
    return Vpasos
def I_S_Totalb2(n):
    Vpasos = []
    permutations = permutaciones(n)

    for i in permutations:
        salida = insertionSort4(list(i))
        Vpasos.append(salida)
    return Vpasos
def I_S_Totalb3(n):
    Vpasos = []
    permutations = permutaciones(n)

    for i in permutations:
        salida = insertionSort5(list(i))
        Vpasos.append(salida)
    return Vpasos
def I_S_Totalb4(n):
    Vpasos = []
    permutations = permutaciones(n)

    for i in permutations:
        salida = insertionSort6(list(i))
        Vpasos.append(salida)
    return Vpasos

s1 = I_S_Totalb(3)
s2 = I_S_Totalb2(3)
s3 = I_S_Totalb3(3)
s4 = I_S_Totalb4(3)
print("numero de intrucciones")
plt.figure(7)
plt.hist(s1,50,facecolor='g')
plt.show()
print("numero de swaps")
plt.figure(8)
plt.hist(s2,50,facecolor='g')
plt.show()
print("numero de preguntas en el while")
plt.figure(9)
plt.hist(s3,50,facecolor='g')
plt.show()
print("numero de comparaciones")
plt.figure(10)
plt.hist(s4,50,facecolor='g')
plt.show()
r = permutaciones(3)
#######################################################
#   usando el codigo de daniel jumenez
#######################################################
print("Usando el código de daniel jimenez")

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

def isortSteps(a):
    v = []
    for i in range(len(a)):
        v.append(a[i])

    steps = 0
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while (j > -1) and (v[j] > x):
            v[j+1] = v[j]
            j = j -1
            steps = steps + 3
        steps = steps + 1
        v[j+1] = x
        steps = steps + 4
    steps = steps + 1
    return steps


n = 100
runs = 10000

sum = 0
min = n**3
max = 0
for i in range(runs):
    t = isortSteps(randomPerm(n))
    print (t)
    if t < min :
       min = t
    if t > max :
       max = t
    sum = sum + t
print ('Theoretical best time, ' + str(5*n - 4))
print ('Theoretical worst time,' + str((3.0/2.0)*n**2 + (7.0/2.0)*n - 4))
print ('Theoretical average time,' + str((3.0/4.0)*n**2 + (17.0/4.0)*n - 4))
print ('Experimenal best time, ' + str(min))
print ('Experimenal worst time,' + str(max))
print ('Experimenal average time,' + str(sum/runs))
