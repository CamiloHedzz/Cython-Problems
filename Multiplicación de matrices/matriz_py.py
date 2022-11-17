def producto_matrices_py(a, b,dimension):    
    producto = []
    for i in range(dimension):
        producto.append([])
        for j in range(dimension):
            producto[i].append(None)
    
    for c in range(dimension):
        for i in range(dimension):
            suma = 0
            for j in range(dimension):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
