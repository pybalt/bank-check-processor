""" 
Este sera el algoritmo principal. Llamara a sus dependencias (/recursos)
y primero leera el .json. Luego lo parcheara a un formato interpretable por python.
Luego lo procesara y creara el(los) .HTML de salida.

Entonces, el usuario solamente hara lo siguiente:
1.  Debe de colocar este archivo en la misma carpeta que el .json
2.  Debe ejecutar este main.py
3.  El main.py se ejecuta (no tiene ningun tipo de interfaz de usuario)
4.  Al terminar la ejecucion spawnea un HTML (o varios)
        a. El(los) HTML debe de tener estilo en linea, para evitar crear un CSS aparte para cada html.
        b. Preferentemente, el estilo del HTMl no debe depender de tener conexion a internet.
"""

if '__main__' == '__name__':
        #* Del paquete recursos, importar todo
        #* Algoritmo 👇.
        #! Llama al JSON
        #! Guarda el JSON en una variable
        #! Esa variable la convierte en una clase Cliente
        #! Dentro de la clase cliente, hay un parametro que es una lista (TRANSACCIONES)
        #! Por cada elemento de esa lista, se crea un objeto de clase Transaccion
        #! Se guarda cada uno de esos objetos en una lista.
        #? Ejemplo en test.py 👆
        #! Se procesa cada uno de esos objetos de la lista, se lee si "ACEPTADA" o "FALLIDA"
        #! Si "FALLIDA", entonces se crea una clase de tipo Razon.
        #! La clase de tipo Razon analiza el objeto y devuelve un string con la razon
        #! Se crea una variable con un string de formato HTML(con estilo incluido)
        #! Se crea un archivo de tipo .html que contiene la variable mencionada arriba
        #! Se cierra el programa