#Parte 1:
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

Algoritmo 4: Consultar una cuenta 
consultar(c:CUENTA): REAL
    precondición 
    c.saldo ≠ NULO 

    realizacion 
    resultado = c.saldo 

    postcondicion
    resultado = c.saldo
fin consultar 

