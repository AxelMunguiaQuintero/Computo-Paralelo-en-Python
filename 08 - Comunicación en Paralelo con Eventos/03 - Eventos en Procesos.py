# Importar librerías
import multiprocessing
import time

# Definir funciones
def esperar_bandera(event: multiprocessing.Event) -> None:
    
    """
    Función que ejecuta el resto del código una vez que la bandera del Evento sea igual a True.
    """
    
    # Esperar
    print("Esperando por el cambio de estado")
    if not event.is_set(): # Esperar en lugar de ejecutar un bucle infinito
        event.wait() # El código se congelará hasta que sea establecido a True (cambiar su estado interno)
    print("Espera ha finalizado")
    
def cambiar_estado(event: multiprocessing.Event) -> None:
    
    """
    Espera un tiempo para cambiar el estado de la bandera interna del Evento
    """
    
    time.sleep(5)
    # Cambiar estado de la bandera
    event.set()
    print("Estado inicial ha cambiado")
    
    
if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    
    # Definir Evento
    event = multiprocessing.Event()
    
    # Tiempo Actual + 10 segundos
    tiempo_objetivo = time.time() + 10
    # Bucle Infinito
    while True:
        if time.time() >= tiempo_objetivo:
            # Establecer bandera interna en True
            print("Set")
            event.set()
        if event.is_set():
            # Salir del bucle
            print("Saliendo del bucle")
            break
        time.sleep(2)
        print("Seguir esperando...")
        
    print("\nEjemplo con Procesos\n")
    
    # Inicializar
    t1 = multiprocessing.Process(target=esperar_bandera, args=(event, ))
    t2 = multiprocessing.Process(target=cambiar_estado, args=(event, ))
    t1.start()
    t2.start()
    # Join
    t1.join()
    # Reiniciar el estado de la bandera
    event.clear()  
    print(event.is_set())
    
    # Recordatorio:
    #   - Los Eventos son objetos que se utilizan para la comunicación entre distintos Procesos o dentro del mismo.
    #     Son útiles, pues permiten la sincronización y la señalización de diferentes tareas que se pueden estar 
    #     ejecutando de manera paralela.
