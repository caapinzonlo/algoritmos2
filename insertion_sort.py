import math
import numpy

def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue


def insertionSort2(list):
    retorno = list
    for i in range(1,len(retorno)):
        ValorC = retorno[i]
        posicion = i
        while posicion>0 and retorno[posicion-1]<ValorC:
            retorno[posicion]=retorno[posicion-1]
            posicion = posicion-1
            retorno[posicion]=ValorC

    return retorno
def EncontrarValor(list,n):
    retorno = []
    for i in range(0,len(list)):
        if list[i]==n:
            retorno = i
    if len(retorno)==0:
        retorno = 'NIL'
    return retorno
alist = [31,41,59,2]
r = 0
#insertionSort(alist)
sal = insertionSort2(alist)
print(alist)
print(sal)
retorno = EncontrarValor(alist,5)
print(retorno)
i = math.log(3,2)
if int(i)<i:
    s = int(i)+1
else:
    s = int(i)
print(s)

def sumaBinaria(A,B):
    int_Total = A+B
    i = math.log(int_Total,2)
    if int(i)<i:
        s = int(i)+1
    else:
        s =int(s)
    C = []
    for j in range(s):
        residuo = int_Total%2
        division = int_Total/2
        if residuo == 1:
            division = division-1
        C.append(residuo)
    return C
C = sumaBinaria(2,3)
print(C)
