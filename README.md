 # Comparación de rendimiento entre Cython y Python

_Este proyecto surge con el fin de evaluar el rendiemiento de python a través de cuatro problemas diferentes, haciendo la comparación en paralelo con Cython para determinar la diferencia de los tiempos de cada una de las pruebas. En los que estan los siguientes algoritmos:_

* Algoritmo de ordenamiento Burbuja
* Multiplicacion de matrices
* Metodo de Monte Carlo para oproximaciones al numero PI
* Algoritmo para calcular el factorial de un numero

**El estudio y analisis de cada algoritmo se encuentra disponible en el siguiente cuaderno de colab: [Cython vs Python](https://colab.research.google.com/drive/1isSH0DHz-3BLqqUs3lsO1P5yN0wacyXu?usp=sharing)**

### Requisitos previos 🔧

_Instalacion Python_

    $ sudo apt-get install Python3

_Instalacion Cython_

    $ sudo apt-get install Cython3
  
_Instalación compilador C_

    $ sudo apt-get install build-essential
  
    $ sudo apt-get install gcc

Proceso de compilación

_Se hace uso de Makefile, por lo que facilita el trabajo al momento de compilar y ejecutar nuestros ficheros, el paso a paso es el siguiente:_
    
    $ make clean
    
    $ make all 

Proceso de ejecución

_Para Cython_

    $ cytho3 -a archivo.pyx -o nombre

_Para Python_

    $ python3 setup.py build_ext --inplace
  
    $ python3 principal.py 
  
 
### Marco Conceptual📋

**CYTHON**

Cython es un lenguaje de programación para simplificar la escritura de módulos de extensión para 
Python en C y C++. Siendo estrictos, la sintaxis de Cython es la misma de Python pero con algunos agregados:

1. Se pueden llamar funciones en C, o funciones/métodos de C++, directamente desde el código en Cython.
2. Es posible usar tipos estáticos en las variables (enteros, flotantes, o cualquier tipo de dato).

**PYTHON**

Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software,
la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente 
y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes. 
El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad 
del desarrollo.


### Bibliografia

_El material bibliografico en el que se basó este proyecto para la realización de pruebas y ejecución del mismo fueron las sguientes_

* [Cython](http://www.dropwizard.io/1.0.2/docs/) - Como pasar correctamente de Python a Cython
* [Python](https://docs.python.org/3/) - Documentación sobre Python
* [Ciencia de datos](https://learn.microsoft.com/es-es/training/modules/explore-analyze-data-with-python/) - Exploración y tratamiento de datos con python

## Autores ✒️

Hecho con ❤️ por
* **Juan Esteban Arias** - *Ingeniero en Ciencias de la Computación e AI* 
* **Juan Camilo Hernández** - *Ingeniero en Ciencias de la Computación e AI*
* **Christian David Jimenez** - *Ingeniero en Ciencias de la Computación e AI* 
