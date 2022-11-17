import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def producto_matrices_cy(double[:,:] u, double[:, :] v, double[:, :] res):
    cdef int i, j, k
    cdef int m, n, p

    m = u.shape[0]

    with cython.nogil:
        for i in range(m):
            for j in range(m):
                res[i,j] = 0
                for k in range(m):
                    res[i,j] += u[i,k] * v[k,j]