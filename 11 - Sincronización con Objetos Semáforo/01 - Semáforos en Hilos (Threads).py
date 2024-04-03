# Importar librerías
import threading
import time
from numpy import random


# Definir función
def modificar_bd(num_aplicacion: str) -> None:
    
    """
    Función que simula el acceso y modificación a una base de datos
    """
    
    # Adquirir
    sem.acquire()
    print(f"Aplicación No. {num_aplicacion} está accediendo y modificando la base de datos")
    # Dormiremos tiempo aleatorio
    time.sleep(random.randint(low=3, high=11, size=1, dtype=int)[0])
    print(f"Aplicación No, {num_aplicacion} ha terminado")
    sem.release()
    

# Definir semáforo
sem = threading.Semaphore(value=3) # Definir número máximo de Hilos que lo pueden acceder al mismo tiempo
# Inicializar Hilos
t0 = threading.Thread(target=modificar_bd, args=("1", ))
t1 = threading.Thread(target=modificar_bd, args=("2", ))
t2 = threading.Thread(target=modificar_bd, args=("3", ))
t3 = threading.Thread(target=modificar_bd, args=("4", ))
t0.start(); t1.start(); t2.start(); t3.start()
# Join 
t0.join(); t1.join(); t2.join(); t3.join()

# Inconvenientes de los Semáforos:
print("Valor máximo de Semáforo:", sem._value)
sem.release()
print("Valor máximo de Semáforo:", sem._value)
sem.release()
print("Valor máximo de Semáforo:", sem._value)

# Recordatorio:
#   - Los Semáforos son útiles para la administración de recursos.
#   - Un Semáforo es esencialmente un contador que se utiliza para controlar el acceso a un recurso específico.
#   - El contador interno puede ser modificado si se libera en un mayor número de veces que las que se adquiere.
