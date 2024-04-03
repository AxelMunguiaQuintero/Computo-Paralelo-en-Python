# Importar librerías
import multiprocessing
import numpy as np
import time


# Definir funciones
def proceso_1(lista, condicion) -> None:
    
    """
    Función que agrega una serie de valores a un objeto de memoria compartida y notifica que la condición
    ha sido cumplida.
    """ 
    
    # Realizar cambios a lista
    condicion.acquire()
    for i in range(5):
        lista.append(i)
        print(f"Proceso No. 1: Ha agregado {i} a la lista")
        time.sleep(1)
    # Notificar al otro proceso que hemos terminado
    condicion.notify()
    condicion.release()
    print("Proceso 1 ha terminado")
    

def proceso_2(lista, condicion) -> None:
    
    """
    Función que espera a que la condición sea cumplida y posteriormente realiza una serie de calculos.
    """
    
    condicion.acquire()
    # Esperamos a que el proceso 1 termine de agregar los elementos
    condicion.wait()
    # Realizar operaciones
    raiz_cuadrada = np.array(lista[:])**(1/2)
    # Agregar a la lista
    lista.append(raiz_cuadrada)
    print("Proceso No. 2: Lista después de la notificación ->", lista[:])
    print("Proceso 2 ha terminado")  
    condicion.release()
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    
    # Lista de memoria compartida
    manager = multiprocessing.Manager()
    lista_numeros = manager.list([])
    
    # Condición
    condicion = multiprocessing.Condition(lock=multiprocessing.Lock())
    
    # Crear los Procesos
    p1 = multiprocessing.Process(target=proceso_1, args=(lista_numeros, condicion))
    p2 = multiprocessing.Process(target=proceso_2, args=(lista_numeros, condicion))
    
    # Inicializar ambos Procesos 
    p2.start()
    time.sleep(0.1)
    p1.start()
    
    # Esperar a que ambos procesos terminen
    p2.join()
    
    # Recordatorio:
    #   - Los objetos Condicionales permiten una sincronización entre Procesos para coordinar la ejecución
    #     y compartir información de manera segura.
