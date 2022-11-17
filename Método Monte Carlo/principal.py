import time

import number_cy
import number_py

#Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range(1, 5000, 50):

    ini_timepy = time.time()
    number_py.calculopi_py(i)
    fin_timepy = time.time()
    time_python = fin_timepy-ini_timepy

    
    ini_timecy = time.time()
    number_cy.calculopi_cy(i)
    fin_timecy = time.time()
    time_cython = fin_timecy-ini_timecy
    
    with open("numberpi.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))