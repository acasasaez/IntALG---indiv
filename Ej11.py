#Parte 1 
from tkinter.tix import REAL
Definir función rem_horas_extra (salrio_bruto: REAL, horas_ext: ENTERO) REAL
    precondición:
    salrio_bruto > 0
    horas_ext > 0

    constantes: 
    CANTIDAD_SEMANAS (ENTERO) = 52
    #número de semanas de trabajo
    CANTIDAD_HORAS_SEMANA(ENTERO) = 35
    #cantidad legal máxima de horas de trabajo semanales
    CANTIDAD_HORAS_MAX_1 (ENTERO) = 8
    #número de cambio de precio de la remuneración
    PRECIO_1 (REAL) = 1,25
    #Tarifa de remuneracion de las primeras horas extra
    PRECIO_2 (REAL) = 1,50
    #tarifa de remuneración del resto de horas extra
    variable: 
    horas_ext_1 (ENTERO)
    #cantidad de horas extra con precio 1 
    horas_ext_2 (ENTERO)
    #cantidad de horas extra con precio 2
    precio_hora (REAL)#precio/hora ded la remuneración bruta básica


    realizazción:
    calcular el precio_hora de la remuneración bruta básica
    Resultado = precio_hora (inf(horas_ext,CANTIDAD_HORS_MAX_1 )* PRECIO_1 + sup(horas_ext - CANTIDAD_HORAS_MAX_1, 0)* PRECIO_2)

    