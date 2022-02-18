#Parte 1 
from tkinter.tix import REAL


Definir MEDIA (n1: REAL, n2: REAL, n3: REAL) REAL #DEFINIMOS LA FUNCIÓN SUMA
    suma = n1 + n2 + n3 #INICIALMENTE NUESTRA FUNCIÓN SUMA LOS TRES PARÁMETROS APORTADOS
    media = suma/ 3 #NUESTRA FUNCIÓN DIVIDE EL RESULTADO DE SUMA ENTRE 3 PARA OBTENER LA MEDIA
    resultado = suma #NUESTRA FUNCIÓN NOS DEVUELVE LA MEDIA DE LOS TRES NÚMEROS QUE SE INTRODUCEN EN LA MISMA

#Parte 2 
Definir MEDIA (p1: REAL, n1: REAL, p2: REAL,n2: REAL, p3: REAL, n3: REAL) REAL
    precondicion
        p1 > 0
        p2> 0
        p3>0
    suma = p1*n1 + p2*n2 + p3*n3 #Inicialmente necesitamos que nuestra función multiplique cada valor por su peso y los sume 
    media = suma/ (p1 + p2 + p3) #A continuación nuestra función dividirá la suma entre la suma del peso de cada elemento
    resultado = media # Finalmente nuesstra función debe devilvernos el valor de la media ponderada de nuestros tres números
