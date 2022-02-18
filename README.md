# IntALG---indiv
Para realizar la tarea, como siempre, he comenzado por realizar un repositorio, adjunto enlace: 

Los ejercicios son los siguientes:

Ejercicio 1: constaba de dos partes. La primera consistía en definir un algoritmo que nos permitiese calcular el el IVA (dado) sobre un precio bruto. La segunda parte consistía en elaborar un algoritmo que nos permitiese calcular el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, expresado en meses.

Ejercicio 2:este ejercicio también cuenta con 2 partes. En la primera se nos pedía calcular una media aritmética y en la segunda calcular una media aritmética ponderada (en ambos casos de 3 números dados).

Ejercicio 3: en este apartado del trabajo se pedía escribir un algoritmo que calculase el área de un triángulo a partir de una base y altura dadas. También se nos preguntaba si a partir de conocer la longitud de los lados perpendiculares de un triángulo rectángulo se podría emplear nuestro algoritmo para hallar el área de dicho triángulo.

En cuanto a los ejercicios 11 y 12 no tenía ni idea de cómo realizarlos, especialmente el 12, ya que no entendía los enunciados, por lo tanto tampoco sabría hacer una descripción propia al respecto de dichos algoritmos. 

"COPIO Y PEGO ENUNCIADOS"


El cálculo de una nómina tiene en cuenta el salario bruto asociado a las horas «normales» que debe hacer el empleado y las horas «extra» trabajadas en el mes. Las horas extra se remuneran según las siguientes normas administrativas:

Tarifa por hora aumentada en un 125 % para las horas entre la 36.ª y la 43.ª.

Tarifa por hora aumentada en un 150 % para las horas a partir de la 44.ª.

El aumento se realiza sobre la tarifa por hora normal, calculado a partir del salario mensual bruto para un año de 52 semanas repartidas en 12 meses, sobre la base de 35 horas trabajadas por semana.

Escribir el algoritmo que calcula el importe de las horas extra que hay que pagar, a partir del salario mensual bruto y de la cantidad de horas extra.

Se podrá suponer que el cálculo siempre se usa para una cantidad de horas superior a 8. El problema general supone el estudio previo del capítulo siguiente, que trata de la alternativa.

Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.

``` #Primera parte ejercicio

definir Precio (p1: REAL): REAL #p1 es nuestro impuesto sin IVA
    p2 = float (input ("Introducir el porcentajede impuesto")) #p2 será el porcentaje de IVA añadido
    preciofinal = p1 + (p1*p2) #calculamos el valor del producto con IVA
    resultado = preciofinal #La función nos devuelve el precio con el IVA añadido
fin Precio
#Segunda parte ejercicio

definir importe (capital: REAL, intereses: PORCENTAJE, meses: ENTERO) REAL #Definimos nuestra función
    precondicion:
    capital > 0
    interses > 0
    meses > 0
    importefinal = (capital*intereses)*meses #Calculamos en os x meses daados cuánto será el importe de los intereses
    resultado = importefinal # La función nos devuelve un valor real que equivale al total de la suma de los intereses dados a lo largo de los x meses 
fin importe


#Parte 1 
from msilib.schema import Media
from tkinter.tix import REAL


Definir MEDIA (n1: REAL, n2: REAL, n3: REAL) REAL #DEFINIMOS LA FUNCIÓN SUMA
    suma = n1 + n2 + n3 #INICIALMENTE NUESTRA FUNCIÓN SUMA LOS TRES PARÁMETROS APORTADOS
    media = suma/ 3 #NUESTRA FUNCIÓN DIVIDE EL RESULTADO DE SUMA ENTRE 3 PARA OBTENER LA MEDIA
    resultado = suma #NUESTRA FUNCIÓN NOS DEVUELVE LA MEDIA DE LOS TRES NÚMEROS QUE SE INTRODUCEN EN LA MISMA
fin MEDIA 

#Parte 2 
Definir MEDIA (p1: REAL, n1: REAL, p2: REAL,n2: REAL, p3: REAL, n3: REAL) REAL
    precondicion
        p1 > 0
        p2> 0
        p3>0
    suma = p1*n1 + p2*n2 + p3*n3 #Inicialmente necesitamos que nuestra función multiplique cada valor por su peso y los sume 
    media = suma/ (p1 + p2 + p3) #A continuación nuestra función dividirá la suma entre la suma del peso de cada elemento
    resultado = media # Finalmente nuesstra función debe devilvernos el valor de la media ponderada de nuestros tres números
fin MEDIA


Definir AREA (b: REAL,h: REAL) REAL #Comenzamos definiendo nuestra función
    precondicion
        b>0
        h>0
    #Nuestra función tiene que aplicar la fórmula del área del triánulo
    mult = b*h #Para esto comienza multiplicando la base por la altura (valores dados)
    area = mult/2 #y finalmente divide el resultado mult entre 2
    resultado = area # para terminar, esta debe devolvernos el resultado del área de nuestro triángulo
fin AREA
#RESPUESTA A LA PREGUNTA
#Sí, pues tenemos en cuenta que si posicionamos uno de los lados perpendiculares como base el otro corresponde a la altura, de este modo, podemos obtener el área del triángulo rectángulo a partir de la longitud de los lados perpendiculares mediante nuestro algoritmo


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

    postcondicion:
    Resultado = precio_hora (inf(horas_ext,CANTIDAD_HORS_MAX_1 )* PRECIO_1 + sup(horas_ext - CANTIDAD_HORAS_MAX_1, 0)* PRECIO_2)
fin rem_horas_extra


#Parte 1:
from argparse import BooleanOptionalAction
from asyncio import current_task
from msilib.schema import Directory
from tkinter.messagebox import ABORTRETRYIGNORE
from tkinter.tix import REAL

from pkg_resources import NullProvider


tipo CUENTA estructura
    saldo: REAL
    descubierto: REAL

    invariante
        #El descubierto no está autorizado
        descubierto = 0
        #El saldo debe ser superior al descubierto autorizado
        saldo >= descubierto
fin CUENTA

Algoritmo 1: Definición de abrir CUENTA
abrir( c:CUENTA, saldo_inicial: REAL)
    precondición: 
    saldo_inicial > 0

    realización:
    c.descubierto = 0
    c.saldo = saldo_inicial

    postcondicion
    c.descubierto = 0
        #no está autorizado
        antiguo (saldo_inicial) = saldo_inicial
        c.saldo = saldo_inicial
fin abrir 

#Parte2
Algoritmo 2: Abonar una cuenta 
abonar(c:CUENTA, credito: REAL))
    precondicion
    c.saldo ≠ NULO 
    crédito ≠ NULO 

    realizacion
    c.saldo = c.saldo + credito 

    postcondicion
    #El descubierto autorizado y el importe del crédito no se modifican
    antiguo(c).descubierto = descubierto
    antiguo(c).credito = credito 

    #El saldo aumenta con el credito 
    c.saldo = antiguo(c).saldo + credito 
fin abonar 

#Parte 3
Algoritmo 3: Cargar una cuenta 
cargar (c: CUENTA, debito: REAL)

    precondicion 
    c.saldo ≠ NULO 
    debito ≠ NULO 
    c.saldo + c.descubierto >= debito >= 0

    realización
    abonar (c, -debito)

    postcondicion
    #El descubierto autorizado y el importe del debito no se modifican 
    antiguo(c).descubierto = descubierto
    antiguo (debito) = debito 

    #Al saldo se le resta el debito 
    c.saldo = antiguo(c).saldo - debito
fin cargar 

#Parte 4
Algoritmo 4: Consultar una cuenta 
consultar(c:CUENTA): REAL
    precondición 
    c.saldo ≠ NULO 

    realizacion 
    resultado = c.saldo 

    postcondicion
    resultado = c.saldo
fin consultar 

#Parte 5
Algoritmo 5: Dfinición es_acredora y es_deudora 
es_acredora (c:CUENENTA): BOOLEANO 
    precondicion 
    c.saldo ≠ NULO 

    realizacion 
    resultado = (c.saldo >= 0)

    postcondicion
    resultado = (c.saldo >= 0)

fin es_acredora


es_deudora (c:CUENENTA): BOOLEANO 
    precondicion 
    c.saldo ≠ NULO 

    realizacion 
    resultado = (-c.saldo <= c.saldo <=0)

    postcondicion
    resultado = (-c.saldo <= c.saldo <=0)

fin es_deudora


#2 DESCUBIERTO AUTORIZADO
#Parte 1
tipo CUENTA estructura
    saldo: REAL
    descubierto: REAL

    invariante
        #El descubierto está autorizado
        descubierto >= 0
        #El saldo debe ser superior al descubierto autorizado
        saldo >= descubierto
fin CUENTA

Algoritmo 1: Definición de abrir CUENTA
abrir( c:CUENTA, saldo_inicial: REAL)
    precondición: 
    saldo_inicial > 0
    descubierto_MAX >= 0

    realización:
    c.descubierto = descubierto_MAX
    c.saldo = saldo_inicial

    postcondicion
    c.descubierto = descubierto_MAX
    c.saldo = saldo_inicial
fin abrir 

#3 CUENTA Y TIEMPO
#Parte 1
tipo CUENTA estructura
    saldo: REAL
    descubierto: REAL
    fecha_descubierto: FECHA #Fecha de inicio del último descubierto
    duracion_max : FECHA #Duración máxima del descubierto

    invariante
        #El descubierto está autorizado durante un tiempo limitado
        descubierto >= 0
        fecha_descubierto ≠ 0 => fecha_descubierto + duracion_max <= fecha_actual
        #El saldo debe ser superior al descubierto autorizado
        saldo >= descubierto
fin CUENTA

#Partedo 
Algoritmo 2:Definición de abrir cuenta 
abrir 
    Entrada 
    c: CUENTA
    saldo_inicial: REAL 
    descubierto_MAX: REAL
    duracion_MAX: FECHA

    Precondicion:
    saldo_inicial> 0
    descubierto_MAX >=0
    duracion_MAX >= 0

    Realizacion
    c.descubierto = c.desubierto_MAX
    c.saldo = saldo_inicial
    d.fecha_descubierto = 0
    c.duracion_max = duracion_max

    postcondicion:
    c.descubierto = c.desubierto_MAX
    c.saldo = saldo_inicial
    d.fecha_descubierto = 0
    c.duracion_max = duracion_max
fin abrir


En cuanto a los UML: me he puesto un poco tarde con la tarea y no me ha dado tiempo ha realizarlos, de todos modos llevo pensándolos unos días y el único ejercicio en el que encuentro sentido realizar un diagrama de clases es en el último y como no entiendo el enunciado se me ha complicado el hacerlo.

Por último dejo por aquí mis "pseudocódigos"
