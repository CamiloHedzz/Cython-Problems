import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def ord_burbuja_cy(arreglo):
    cdef int n = len(arreglo)
    cdef int i, j
    for i in range(n-1):       
        for j in range(n-1-i): 
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]