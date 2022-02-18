from tkinter.tix import REAL


definir Precio (p1: REAL): REAL #p1 es nuestro impuesto sin IVA
    p2 = float (input ("Introducir el porcentajede impuesto")) #p2 será el porcentaje de IVA añadido
preciofinal = p1 + (p1*p2) #calculamos el valor del producto con IVA
resultado = preciofinal #La función nos devuelve el precio con el IVA añadido