# Importar librerías
import threading
import time


# Definir funciones
def participantes(nombre: str) -> None:
    
    """
    Función que simula la llegada del participante a una conferencia.
    """
    
    # Simular el tiempo de llegada
    print(f"{nombre} ha llegado a la sala y está revisando sus notas")
    
    # Esperaremos a que todos los participantes lleguen
    barrera.wait()
    
    # Iniciar la presentación
    print("¡La presentación ha comenzado!")
    

def presentacion() -> None:
    
    """
    Simula el inicio de una presentación
    """
    
    print("\nLa presentación ahora puede comenzar\n")
    
    
# Crear una barrera para 5 personas/participantes
barrera = threading.Barrier(parties=5, action=presentacion)

# Crear cada participantes (Hilo)
participante1 = threading.Thread(target=participantes, args=("Participante 1",))
participante2 = threading.Thread(target=participantes, args=("Participante 2",))
participante3 = threading.Thread(target=participantes, args=("Participante 3",))
participante4 = threading.Thread(target=participantes, args=("Participante 4",))
participante5 = threading.Thread(target=participantes, args=("Participante 5",))

# Inicializar (Simular la hora de llegada)
participante1.start()
time.sleep(1.0)
participante2.start()
time.sleep(0.5)
participante3.start()
time.sleep(1.5)
participante4.start()
participante5.start()

# Esperar a que todos los participantes terminen
participante1.join()
participante2.join()
participante3.join()
participante4.join()
participante5.join()

# Recordatorio:
#   - Las Barreras son un punto de encuentro para todos los Hilos. Son útiles para sincronizar en una parte
#     de nuestro código a todos los programas que se están ejecutando en paralelo.
    