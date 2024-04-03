# Importar librerías
import threading
import time


# Definir Evento
event = threading.Event()
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
    
print("\nEjemplo con Hilos\n")

# Ejemplo usando Hilos
event = threading.Event()
def esperar_bandera() -> None:
    
    """
    Función que ejecuta el resto del código una vez que la bandera del Evento sea igual a True.
    """
    
    # Esperar
    print("Esperando por el cambio de estado")
    if not event.is_set(): # Esperar en lugar de ejecutar un bucle infinito
        event.wait() # El código se congelará hasta que sea establecido a True (cambiar su estado interno)
    print("Espera ha finalizado")
    
def cambiar_estado() -> None:
    
    """
    Espera un tiempo para cambiar el estado de la bandera interna del Evento
    """
    
    time.sleep(5)
    # Cambiar estado de la bandera
    event.set()
    print("Estado inicial ha cambiado")
    
    
# Inicializar
t1 = threading.Thread(target=esperar_bandera, args=())
t2 = threading.Thread(target=cambiar_estado, args=())
t1.start()
t2.start()
# JOIN
t1.join()
# Reiniciar el estado inicial del Evento
event.clear() 
print(event.is_set())

# Recordatorio:
#   - Los Eventos son objetos que se utilizan para la comunicación entre distintos Hilos o dentro del mismo.
#     Son útiles, pues permiten la sincronización y la señalización de diferentes tareas que se pueden estar 
#     ejecutando de manera paralela.
    