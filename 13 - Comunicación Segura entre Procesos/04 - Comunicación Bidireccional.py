# Importar librerías
import multiprocessing
import time
import numpy as np
import pandas as pd


# Definir funciones
def Tuberia_Inicial(pipe_inicial) -> None:
    
    """
    Función que se usará para una comunicación bidireccional
    """
    
    while True:
        # Enviar un mensaje con distintos tipos de estructuras de datos
        datos = ["Lado Inicial", time.time(), np.array([1, 2, 3]), pd.DataFrame(data=[1,2,3], columns=["Inicial"])]
        pipe_inicial.send(datos)
        # Esperar a recibir datos
        datos_recibidos = pipe_inicial.recv()        
        print("Datos recibidos en cola inicial:", datos_recibidos)
        time.sleep(3)


def Tuberia_Final(pipe_final) -> None:
    
    """
    Función que se usará para una comunicación bidireccional
    """
    
    while True:
        # Esperar a recibir datos
        datos_recibidos = pipe_final.recv()     
        # Enviar un mensaje con distintos tipos de estructuras de datos
        datos = ["Lado Final", time.time(), np.array([4, 5, 6]), pd.DataFrame(data=[4,5,6], columns=["Final"])]
        pipe_final.send(datos)
        print("Datos recibidos en cola Final:", datos_recibidos)
        time.sleep(3)
        
    
if __name__ == "__main__":
    # Método
    multiprocessing.set_start_method("spawn")
    pipe_ini, pipe_fin = multiprocessing.Pipe(duplex=True)
    p0 = multiprocessing.Process(target=Tuberia_Inicial, args=(pipe_ini,))
    p1 = multiprocessing.Process(target=Tuberia_Final, args=(pipe_fin,))
    p0.start()
    p1.start()
    # Dormiremos 10 segundos
    time.sleep(10)
    p0.kill()
    p1.kill()
    
    print("\n Programa ha finalizado \n")
        
    # Recordatorio:
    #   - Los Pipes en Python permiten establecer comunicación bidireccional entre Procesos, lo que significa que ambos extremos
    #     del pipe pueden ser utilizados para enviar y recibir datos.
    #   - Los Pipes facilitan la sincronización entre Procesos al permitir que uno espere a que el otro envíe o reciba datos. Esto
    #     es muy útil para coordinar la ejecución de procesos concurrentes.
    #   - La comunicación a través de pipes es segura para datos serializables. Python automáticamente serializa y deserializa los datos
    #     que se envían a través de pipes, garantizando una comunicación efectiva entre Procesos.
