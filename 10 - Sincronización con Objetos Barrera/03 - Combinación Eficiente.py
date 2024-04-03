# Importar librerías
import multiprocessing
import threading
import time


# Definir funciones
def atleta(nombre: str, hilo_barrera: threading.Barrier) -> None:
    
    """
    Simular el calentamiento de un equipo.
    """
    
    print(f"{nombre} esta realizando entrenamiento")
    
    # Esperar a que todos los atletas del equipo completen su entrenamiento
    hilo_barrera.wait()
    
    
def equipo(nombre: str, proceso_barrera: multiprocessing.Barrier) -> None:
    
    """
    Simula el calentamiento de los atletas de un equipo
    """
    
    print(f"Equipo {nombre} está preparando a sus atletas")
    
    # Barrera Hilos
    barrera = threading.Barrier(2, action=calentamiento_terminado)
    # Crear Hilos
    atleta1 = threading.Thread(target=atleta, args=(f"Atleta 1 del Equipo {nombre}", barrera))
    atleta2 = threading.Thread(target=atleta, args=(f"Atleta 2 del Equipo {nombre}", barrera))
    # Inicializamos
    atleta1.start()
    atleta2.start()
    
    print(f"Equipo {nombre} está listo para la compentencia principal")
    
    # Esperar a los otros equipos
    proceso_barrera.wait()


def compentencia_principal() -> None:
    
    """
    Simular el inicio de la competencia
    """
    
    print("¡Todos los equipos están listos! Comienza la competencia principal")
    

def calentamiento_terminado() -> None:
    
    """
    Simular el calentamiento completado de un equipo
    """
    
    print("¡Otro equipo ya está listo para competir!")
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    
    # Crear una barrera para 4 equipos
    barrera = multiprocessing.Barrier(parties=4, action=compentencia_principal)
    
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

    # Recordatorio:
    #   - Las Barreras son útiles para sincronizar código en un punto.
    #   - Las arquitecturas tanto en threading como en multiprocessing se pueden combinar, sin embargo,
    #     la complejidad de nuestro programa crece a medida que distintas arquitecturas se suman.
