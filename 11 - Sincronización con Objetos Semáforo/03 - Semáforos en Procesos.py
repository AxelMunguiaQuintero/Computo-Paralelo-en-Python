# Importar librerías
import multiprocessing
import time
from numpy import random


# Definir función
def atender_clientes(sem, cliente) -> None:
    
    """
    Simular la atención a clientes
    """
    
    sem.acquire()
    print(f"Un agente está atendiendo al cliente {cliente}")
    tiempo_atencion = random.randint(3, 10) 
    time.sleep(tiempo_atencion)
    print(f"El agente ha terminado su trabajo con {cliente}")
    sem.release()
    

if __name__ == "__main__":
    
    # Establcer método
    multiprocessing.set_start_method("spawn")
    # Número de agentes disponibles
    num_agentes = 3
    # Crear semáforo
    sem = multiprocessing.Semaphore(value=num_agentes)
    # Representar a cada cliente como un Proceso
    numero_clientes = 7
    procesos_clientes = []
    for i in range(numero_clientes):
        p = multiprocessing.Process(target=atender_clientes, args=(sem, i))
        procesos_clientes.append(p)
        p.start()
    # Esperar la ejecución de los Procesos
    for i in procesos_clientes:
        i.join()
        
    # Inconvenientes de los Semáforos:
    print("Valor máximo de Semáforo:", sem.get_value())
    sem.release()
    print("Valor máximo de Semáforo:", sem.get_value())
    sem.release()
    print("Valor máximo de Semáforo:", sem.get_value())
    
    # Recordatorio:
    #   - Los Semáforos son útiles para la administración de recursos.
    #   - Un Semáforo es esencialmente un contador que se utiliza para controlar el acceso a un recurso específico.
    #   - El contador interno puede ser modificado si se libera en un mayor número de veces que las que se adquiere.
