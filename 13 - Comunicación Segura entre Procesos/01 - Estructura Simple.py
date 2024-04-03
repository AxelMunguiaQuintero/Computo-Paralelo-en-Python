# Importar librerías
import multiprocessing
import pandas as pd
import numpy as np
import time


# Definir funciones
def recibir_datos(cola_simple) -> None:
    
    """
    Recibir diferentes tipos de datos y los imprime por pantalla
    """
    
    # Recibir datos
    while True:
        mensaje_privado = cola_simple.get()
        if mensaje_privado is None:
            break
        else:
            for i in mensaje_privado:
                print("Tipo de Dato:", type(i))
                print("Dato:", i)
        # Dormir en cada iteración
        time.sleep(2)
        print("\n -------- \n")
        
def mandar_datos(datos, cola_simple) -> None:
    
    """
    Encolar datos a la cola simple
    """
    
    # Mandar datos
    cola_simple.put(datos)
    

if __name__ == "__main__":
    
    # Establecer el método
    multiprocessing.set_start_method("spawn")
    # Crear un objeto de Cola Simple
    cola_simple = multiprocessing.SimpleQueue()
    # Crear 3 Procesos para agregar los datos
    procesos = []
    for i in range(3):
        cadena_texto = "Hola"
        datos_numpy = np.random.randint(0, 10, size=(2, 5))
        serie_pandas = pd.DataFrame(data= np.random.randint(5, 50, size=(5, 1)), columns=["Serie"])
        datos = [cadena_texto, datos_numpy, serie_pandas]
        p = multiprocessing.Process(target=mandar_datos, args=(datos, cola_simple))
        procesos.append(p)
        p.start()
    # Esperar a que se termine de mandar todos los datos
    for i in procesos:
        i.join()
    # Cesar la ejecución
    cola_simple.put(None)
    # Levantar Proceso que reciba la información
    p = multiprocessing.Process(target=recibir_datos, args=(cola_simple,))
    p.start()
    # Esperar a que termine
    p.join()
    
    # Recordatorio:
    #   - Las Colas son herramientas altamente efectivas para la transmisión de información de manera ordenada y segura.
    #   - Nos permiten transmitir datos entre Procesos de una manera más eficiente y rápida que con objetos de memoria compartida.
