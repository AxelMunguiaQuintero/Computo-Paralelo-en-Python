# Importar librerías
import multiprocessing
import time


# Definir funciones
def equipo(nombre: str, barrera: multiprocessing.Barrier) -> None:
    
    """
    Función que simula la llegada de cada grupo.
    """
    
    # Simulando la llegada del equipo
    print(f"Equipo {nombre} está listo para correr")
    
    # Esperar a que todos los equipos estén listos
    barrera.wait()
    
    # Comenzar la carrera
    print(f"La carrera ha comenzado para el Equipo {nombre}")
    

def iniciar_carrera() -> None:
    
    """
    Simular el inicio de la carrera
    """
    
    print("\nEmpieza la carrera\n")
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    
    # Crear una barrera para 4 equipos
    barrera = multiprocessing.Barrier(parties=4, action=iniciar_carrera)
    
    # Definir equipos (Procesos)
    p1 = multiprocessing.Process(target=equipo, args=("A", barrera))
    p2 = multiprocessing.Process(target=equipo, args=("B", barrera))
    p3 = multiprocessing.Process(target=equipo, args=("C", barrera))
    p4 = multiprocessing.Process(target=equipo, args=("D", barrera))
    
    # Inicializar equipos
    p4.start()
    time.sleep(2)
    p2.start()
    time.sleep(1)
    p1.start()
    time.sleep(2)
    p3.start()
    
    # Esperar a que cada participante termine
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    
    print("\nReutlizar Barrera\n")
    
    # Definir equipos (Procesos)
    p5 = multiprocessing.Process(target=equipo, args=("E", barrera))
    p6 = multiprocessing.Process(target=equipo, args=("F", barrera))
    p7 = multiprocessing.Process(target=equipo, args=("G", barrera))
    p8 = multiprocessing.Process(target=equipo, args=("H", barrera))
    
    # Inicializar equipos
    p5.start()
    time.sleep(2)
    p6.start()
    time.sleep(1)
    p7.start()
    time.sleep(2)
    p8.start()
    
    # Esperar a que cada participante termine
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    
    # Recordatorio:
    #   - Las Barreras son un punto de encuentro para todos los Procesos y son útiles para sincronizar en una parte
    #     de nuestro código a todos los programas que están ejecutandose en paralelo.
    #   - Las Barreras pueden ser reutilizadas múltiples veces en un programa.
    