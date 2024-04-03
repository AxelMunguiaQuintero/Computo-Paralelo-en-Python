# Importar librerías
import threading
import time


# Condicional
mutex = threading.Lock()
cv = threading.Condition(lock=mutex)


# Definir funciones
def func0() -> None:
    
    """
    Función que espera a que un condicional se cumpla.
    """
    
    # Adquirir
    cv.acquire()
    print("Func0: Condicional todavía no cumplido")
    # Esperar a que se notifique
    cv.wait() # Realiza un release y espera
    print("Func0: Condicional se ha cumplido")
    cv.release()
    
def func1() -> None:
    
    """
    Función que espera a que un condicional se cumpla.
    """
    
    # Adquirir
    cv.acquire()
    print("Func1: Condicional todavía no cumplido")
    # Esperar a que se notifique
    cv.wait() # Realiza un release y espera
    print("Func1: Condicional se ha cumplido")
    cv.release()
    
def func2() -> None:
    
    """
    Función que espera a que un condicional se cumpla.
    """
    
    # Adquirir
    cv.acquire()
    print("Func2: Condicional todavía no cumplido")
    # Esperar a que se notifique
    cv.wait() # Realiza un release y espera
    print("Func2: Condicional se ha cumplido")
    cv.release()
    

def condicionales_cumplidos() -> None:
    
    """
    Función que simula el cumplimiento del condicional para cada Hilo
    """
    
    # Dormiremos 1 segundos antes de notificar al primer Hilo
    time.sleep(1)
    cv.acquire()
    cv.notify(n=1)
    cv.release()
    
    # Dormimos 5 segundos antes de notificar al segundo Hilo
    time.sleep(5)
    with cv: # El condicional se adquiere y se libera en automático con "with"
        cv.notify(n=1)
        
    # Noticamos a todos los restantes (en este caso es solo 1)
    time.sleep(8)
    cv.acquire()
    cv.notify_all()
    cv.release()
    
    
# Inicializar
t0 = threading.Thread(target=func0)
t0.start()
t1 = threading.Thread(target=func1)
t1.start()
t2 = threading.Thread(target=func2)
t2.start()
        
# Condicionales cumplidos
condicionales_cumplidos()

# Recordatorio:
#   - Los objetos condicionales son mejores herramientas para comunicarse entre distintos Hilos o Procesos.
#   - Proporcionan una estructura más enriquecida para la comunicación entre distintas aplicaciones.
#   - Se notificará a cada Hilo en el orden en que están en la cola de espera.
