Definir AREA (b: REAL,h: REAL) REAL #Comenzamos definiendo nuestra función
    precondicion
        b>0
        h>0
    #Nuestra función tiene que aplicar la fórmula del área del triánulo
    mult = b*h #Para esto comienza multiplicando la base por la altura (valores dados)
    area = mult/2 #y finalmente divide el resultado mult entre 2
    resultado = area # para terminar, esta debe devolvernos el resultado del área de nuestro triángulo
