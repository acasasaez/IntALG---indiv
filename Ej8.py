from tkinter.tix import REAL
#Primera parte ejercicio

definir Precio (p1: REAL): REAL #p1 es nuestro impuesto sin IVA
    p2 = float (input ("Introducir el porcentajede impuesto")) #p2 será el porcentaje de IVA añadido
preciofinal = p1 + (p1*p2) #calculamos el valor del producto con IVA
resultado = preciofinal #La función nos devuelve el precio con el IVA añadido

#Segunda parte ejercicio

definir importe (capital: REAL, intereses: PORCENTAJE, meses: ENTERO) REAL #Definimos nuestra función
    precondicion:
    capital > 0
    interses > 0
    meses > 0
importefinal = (capital*intereses)*meses #Calculamos en os x meses daados cuánto será el importe de los intereses
resultado = importefinal # La función nos devuelve un valor real que equivale al total de la suma de los intereses dados a lo largo de los x meses 