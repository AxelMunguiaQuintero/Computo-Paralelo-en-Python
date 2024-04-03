# Importar librerías
import threading
import time


# Definir Sincronizador
mutex = threading.Lock() # Bloqueo de exclusión mutua 


# Definir funciones
def hilo1() -> None:
    
    """
    Función que ejecutará el primer Hilo
    """
    
    # Mostrar por consola y adquirir
    print("Dentro del Hilo 1")
    mutex.acquire()
    print("Hilo 1 en posesión")
    time.sleep(3)
    print("Hilo 1 liberando")
    mutex.release()
    
    
def hilo2() -> None:
    
    """
    Función que ejecutará el segundo Hilo
    """
    
    # Mostrar por consola y adquirir
    print("Dentro del Hilo 2")
    mutex.acquire()
    print("Hilo 2 en posesión")
    time.sleep(3)
    print("Hilo 2 liberando")
    mutex.release()
    
    
# Definir Hilos
t1 = threading.Thread(target=hilo1, args=())
t2 = threading.Thread(target=hilo2, args=()) 
t1.start()
t2.start()

# Recordatorio:
#   - Los sincronizadores nos ayudan a coordinar la ejecución de Hilos para realizar tareas u operaciones en un orden
#     definido. Además, son excelentes herramientas para manetener la integridad de los datos.
