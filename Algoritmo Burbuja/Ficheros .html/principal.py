import time

import burbuja_py
import burbuja_cy
#import prueba

import random

formato_datos = "{:.5f},{:.5f}\n"


for i in range(50, 5050, 50):
    #prueba.pruebaa()
    
    
    array = [random.randint(0,1000) for _ in range(i)]
    ini_timepy = time.time()
    burbuja_py.ord_burbuja_py(array)
    fin_timepy = time.time()
    time_python = fin_timepy-ini_timepy


    ini_timecy = time.time()
    burbuja_cy.ord_burbuja_cy(array)
    fin_timecy = time.time()
    time_cython = fin_timecy-ini_timecy
    
    with open("results.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))
    