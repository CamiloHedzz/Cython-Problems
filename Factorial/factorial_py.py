import numpy as np
    
def calculo(numero):
        if numero == 0:
            return 1
        elif numero > 0:
            lower_numbers = []
            while numero > 0:
                lower_numbers.append(numero)
                numero -= 1
            return np.prod(lower_numbers)

