import time

import factorial_cy
import factorial_py

numero = 100000000

facto_py = factorial_py
facto_cy = factorial_cy

formato_datos = "{:0f},{:01f}\n"

for i in range(50000,numero,1000000):

    ini_time_PY = time.time()
    facto_py.calculo(i)
    fin_time_PY = time.time()

    ini_time_CY = time.time()
    facto_cy.calculo(i)
    fin_time_CY = time.time()

    time_cython = fin_time_CY-ini_time_CY 
    time_python = fin_time_PY-ini_time_PY

    with open("factorial2.csv","a") as archivo:
            archivo.write(formato_datos.format(time_python,time_cython))

