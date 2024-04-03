# Importar librerías
import multiprocessing
import time


# Definir función
def proceso_empaque(cola_ensamblaje) -> None:
    
    """
    Simular el proceso de empaquetado
    """
    
    while True:
        producto = cola_ensamblaje.get() 
        if producto == 0:
            break
        print(f"Producto {producto} ha sido liberado y esta siendo empaquetado")
        time.sleep(2)
        

if __name__ == "__main__":
    # Método
    multiprocessing.set_start_method("spawn")
    # Inicializar la Cola FIFO
    cola_ensamblaje = multiprocessing.Queue(maxsize=0)
    # Agregar Productos
    for i in range(15):
        cola_ensamblaje.put(f"Producto_{i}")
        
    print("\n ----- Segmento Informativo -----\n")
    print("Total de objetos en la cola:", cola_ensamblaje.qsize())
    print("Tamaño de nuestra cola:", cola_ensamblaje._maxsize)
    print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_ensamblaje.empty())
    # print("Número de tareas restantes =", cola_ensamblaje.unfinished_tasks)
    print("\n ----- -------------------- -----\n")
    
    # Crear un Hilo para el Proceso de empaque
    proceso = multiprocessing.Process(target=proceso_empaque, args=(cola_ensamblaje,))
    proceso.start()
    
    # Cesar la ejecución
    cola_ensamblaje.put(0)
    
    # Join
    proceso.join()
    
    print("\n ----- Segmento Informativo -----\n")
    print("Total de objetos en la cola:", cola_ensamblaje.qsize())
    print("Tamaño de nuestra cola:", cola_ensamblaje._maxsize)
    print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_ensamblaje.empty())
    # print("Número de tareas restantes =", cola_ensamblaje.unfinished_tasks)
    print("\n ----- -------------------- -----\n")
    
    print("Todos los productos han sido ensamblados, empaquetados y están listos para el envío")

# Recordatorio:
#   - Las colas (Queues) FIFO agregan una mayor cantidad de funcionalidades que permiten limitar el número de elementos
#     que hay en colas y la información relacionada con todo el proceso. Ciertamente agregan mayor complejidad, pero nos
#     permiten crear o simular situaciones de la vida real.
