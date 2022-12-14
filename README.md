 # Comparaci贸n de rendimiento entre Cython y Python

_Este proyecto surge con el fin de evaluar el rendiemiento de python a trav茅s de cuatro problemas diferentes, haciendo la comparaci贸n en paralelo con Cython para determinar la diferencia de los tiempos de cada una de las pruebas. En los que estan los siguientes algoritmos:_

* Algoritmo de ordenamiento Burbuja
* Multiplicacion de matrices
* Metodo de Monte Carlo para oproximaciones al numero PI
* Algoritmo para calcular el factorial de un numero

**El estudio y analisis de cada algoritmo se encuentra disponible en el siguiente cuaderno de Google Colab: [Cython vs Python](https://colab.research.google.com/drive/1isSH0DHz-3BLqqUs3lsO1P5yN0wacyXu?usp=sharing)**


Tambien en el fichero llamado **PythonVsCython.ipynb**

### Requisitos previos 馃敡

_Instalacion Python_

    $ sudo apt-get install Python3

_Instalacion Cython_

    $ sudo apt-get install Cython3
  
_Instalaci贸n compilador C_

    $ sudo apt-get install build-essential
  
    $ sudo apt-get install gcc

Proceso de compilaci贸n

_Se hace uso de Makefile, por lo que facilita el trabajo al momento de compilar y ejecutar nuestros ficheros, el paso a paso es el siguiente:_
    
    $ make clean
    
    $ make all 

Proceso de ejecuci贸n

_Para Cython_

    $ cytho3 -a archivo.pyx -o nombre

_Para Python_

    $ python3 setup.py build_ext --inplace
  
    $ python3 principal.py 
  
 
### Marco Conceptual馃搵

**CYTHON**

Cython es un lenguaje de programaci贸n para simplificar la escritura de m贸dulos de extensi贸n para 
Python en C y C++. Siendo estrictos, la sintaxis de Cython es la misma de Python pero con algunos agregados:

1. Se pueden llamar funciones en C, o funciones/m茅todos de C++, directamente desde el c贸digo en Cython.
2. Es posible usar tipos est谩ticos en las variables (enteros, flotantes, o cualquier tipo de dato).

**PYTHON**

Python es un lenguaje de programaci贸n ampliamente utilizado en las aplicaciones web, el desarrollo de software,
la ciencia de datos y el machine learning (ML). Los desarrolladores utilizan Python porque es eficiente 
y f谩cil de aprender, adem谩s de que se puede ejecutar en muchas plataformas diferentes. 
El software Python se puede descargar gratis, se integra bien a todos los tipos de sistemas y aumenta la velocidad 
del desarrollo.


### Bibliografia

_El material bibliografico en el que se bas贸 este proyecto para la realizaci贸n de pruebas y ejecuci贸n del mismo fueron las sguientes_

* [Cython](http://www.dropwizard.io/1.0.2/docs/) - Como pasar correctamente de Python a Cython
* [Python](https://docs.python.org/3/) - Documentaci贸n sobre Python
* [Ciencia de datos](https://learn.microsoft.com/es-es/training/modules/explore-analyze-data-with-python/) - Exploraci贸n y tratamiento de datos con python

## Autores 鉁掞笍

Hecho con 鉂わ笍 por
* **Juan Esteban Arias** - *Ingeniero en Ciencias de la Computaci贸n e AI* 
* **Juan Camilo Hern谩ndez** - *Ingeniero en Ciencias de la Computaci贸n e AI*
* **Christian David Jimenez** - *Ingeniero en Ciencias de la Computaci贸n e AI* 
