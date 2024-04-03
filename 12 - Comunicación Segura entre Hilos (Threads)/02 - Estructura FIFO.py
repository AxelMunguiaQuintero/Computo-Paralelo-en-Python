# Importar librerías
import threading
import queue
import time


# Definir funciones
def proceso_ensamblaje(producto: str) -> None:
    
    """
    Simular el proceso de ensamblaje en una empresa
    """
    
    # Encolar prodcuto
    cola_ensamble.put(producto)
    print(f"Producto {producto} esta siendo ensamblado y encolado")
    
    
def proceso_empaque() -> None:
    
    """
    Simular el proceso de empaquetado
    """
    
    while True:
        producto = cola_ensamble.get() # Tan pronto se llama esta función se libera un nuevo espacio en la cola
        print(f"Producto {producto} liberado de la cola y siendo empaquetado")
        if producto is None:
            cola_ensamble.task_done()
            break
        time.sleep(2)
        # Avisar que la tarea ya se ha terminado
        cola_ensamble.task_done()
        
# Definir Cola FIFO
cola_ensamble = queue.Queue(maxsize=10) # Máximo de 10 elementos en la cola. Si se agregan más de 10 se deberá esperar
# a que los Hilos adquieran una tarea para poderse liberar.

hilos = []
# Levantar distintos Hilos para ensamblar distintos productor
for i in range(15):
    t = threading.Thread(target=proceso_ensamblaje, args=(f"Producto-{i}", ))
    hilos.append(t)
    t.start()

print("\n ----- Segmento Informativo -----\n")
print("Total de objetos en la cola:", cola_ensamble.qsize())
print("Tamaño de nuestra cola:", cola_ensamble.maxsize)
print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_ensamble.empty())
print("Número de tareas restantes =", cola_ensamble.unfinished_tasks)
print("\n ----- -------------------- -----\n")
    
# Crear Hilo para el proceso de empaque
hilo_empaque = threading.Thread(target=proceso_empaque)
hilo_empaque.start()

# Join
for hilo_ensamblaje in hilos:
    hilo_ensamblaje.join()

# Cesar ejecución
cola_ensamble.put(None)

# Esperar a que termine la ejecución del empaquetado
hilo_empaque.join()

print("\n ----- Segmento Informativo -----\n")
print("Total de objetos en la cola:", cola_ensamble.qsize())
print("Tamaño de nuestra cola:", cola_ensamble.maxsize)
print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_ensamble.empty())
print("Número de tareas restantes =", cola_ensamble.unfinished_tasks)
print("\n ----- -------------------- -----\n")

# Proceso ha terminado
print("¡Todos los productos han sido ensamblados, empaquetados y están listo para el envío!")

# Recordatorio:
#   - Las colas (Queues) FIFO agregan una mayor cantidad de funcionalidades que permiten limitar el número de elementos
#     que hay en colas y la información relacionada con todo el proceso. Ciertamente agregan mayor complejidad, pero nos
#     permiten crear o simular situaciones de la vida real.
