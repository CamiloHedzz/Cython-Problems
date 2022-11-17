import time

import matriz_cy
import matriz_py

import numpy as np

#Se crea un formato para la impresión sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range(1, 1000, 10):

    u = np.random.random((i,i))
    v = np.random.random((i,i))
    res = np.zeros((i,i))

    ini_timepy = time.time()
    matriz_py.producto_matrices_py(u,v, i)
    fin_timepy = time.time()
    time_python = fin_timepy-ini_timepy


    ini_timecy = time.time()
    matriz_cy.producto_matrices_cy(u, v, res)
    fin_timecy = time.time()
    time_cython = fin_timecy-ini_timecy

    with open("matriz.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))
