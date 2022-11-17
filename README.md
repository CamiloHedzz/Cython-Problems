 # Comparación de rendimiento entre Cython y Python

_Este proyecto surge con el fin de evaluar el rendiemiento de python a través de cuatro problemas diferentes, haciendo la comparación en paralelo con Cython para determinar la diferencia de los tiempos de cada una de las pruebas. En los que estan los siguientes algoritmos:_

* Algoritmo de ordenamiento Burbuja
* Multiplicacion de matrices
* Metodo de Monte Carlo para oproximaciones al numero PI
* Algoritmo para calcular el factorial de un numero

### Marco Teorico📋

CYTHON

Cython es un lenguaje de programación para simplificar la escritura de módulos de extensión para 
Python en C y C++. Siendo estrictos, la sintaxis de Cython es la misma de Python pero con algunos agregados:

1. Se pueden llamar funciones en C, o funciones/métodos de C++, directamente desde el código en Cython.
2. Es posible usar tipos estáticos en las variables (enteros, flotantes, o cualquier tipo de dato).

PYTHON

Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software,
la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente 
y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. 
El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad 
del desarrollo.



Requisitos para compilacion:

    $ sudo apt-get install build-essential
  
    $ sudo apt-get install gcc
  

Requisitos para ejecución:

    $ python3 setup.py build_ext --inplace
  
    $ python3 principal.py 
  


Universidad Sergio Arboleda
Autor: Juan Camilo Hernández Ibáñez
