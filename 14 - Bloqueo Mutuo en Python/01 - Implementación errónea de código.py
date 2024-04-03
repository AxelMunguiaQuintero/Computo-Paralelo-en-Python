# Importar librerías
import threading
import time


# Sincronizadores
lock1 = threading.Lock()
lock2 = threading.Lock()

# Definir funciones
def func1() -> None:
    
    """
    Será ejecutada por el Hilo No. 1
    """
    
    lock1.acquire()
    print("Hilo No. 1 ha adquirido el sincronizador 1")
    time.sleep(1)
    print("Hilo No. 1 está esperando el sincronizador 2")
    lock2.acquire()
    print("Hilo No. 1 ha adquirido el sincronizador 2")
    
    # Liberar ambos sincronizadores
    lock1.release()
    lock2.release()
    

def func2() -> None:
    
    """
    Será ejecutada por el Hilo No. 2
    """
    
    lock2.acquire()
    print("Hilo No. 2 ha adquirido el sincronizador 2")
    time.sleep(1)
    print("Hilo No. 2 está esperando el sincronizador 1")
    lock1.acquire()
    print("Hilo No. 2 ha adquirido el sincronizador 1")
    
    # Liberar ambos sincronizadores
    lock2.release()
    lock1.release()
    
    
# Crear e Inicializar Hilos
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2) 
t1.start()
t2.start()

# Joins
t1.join()
t2.join()
    
# Recordatorios:
#   - Los Bloqueos Mutuos o Deadlocks no permitirán que nuestro código se termine de ejecutar.
#   - Una correcta estructura nos puede evitar Bloqueos en nuestra aplicación.
#   - Algunas veces son muy difíciles de identificar.
