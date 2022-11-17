
cimport cython

#IMPORTAR MÓDULO "RANDOM".
import random

from libc.stdlib import rand

cpdef calculopi_cy(int INTERVAL):
    #RANGO
    #INTERVAL= 2000
    
    cdef int circle_points= 0 #PUNTOS DENTRO DEL CÍRCULO 
    cdef int square_points= 0 #PUNTOS DENTRO DEL CUADRADO
    cdef float origin_dist = 0
    cdef float pi = 0
    for i in range(INTERVAL**2):

        #GENERACIÓN DE PUNTOS
        rand_x= rand()
        rand_y= rand()
    
        #DISTANCIA DE CADA PUNTO DEL ORIGEN
        origin_dist= (rand_x**2 + rand_y**2)**0.5
    
        #COMPROBAR SI EL PUNTO ESTÁ DENTRO DEL CÍRCULO.
        if origin_dist<= 1:
            circle_points+= 1
    
        square_points+= 1

        #OBTENCIÓN DEL VALOR DE PI.
        pi = 4* circle_points/ square_points