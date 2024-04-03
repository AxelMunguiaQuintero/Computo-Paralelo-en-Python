# Importar librerías
import threading


# Definir clase
class Reservaciones:
    
    """
    Simula la adquisición de asientos en un cine
    """
    
    def __init__(self, num_asientos: int) -> None:
        
        """
        Constructor.
        """
        
        # Atributos
        self.num_asientos = num_asientos
        self.asientos_disponibles = list(range(1, num_asientos + 1))
        self.sem_asientos = threading.BoundedSemaphore(value=num_asientos)
        
    
    def reservar_asiento(self, nombre_cliente: str) -> None:
        
        """
        Simular la reservación de un asiento en el cine
        """
        
        self.sem_asientos.acquire()
        if len(self.asientos_disponibles) > 0:
            # Los asientos se reservan en orden
            asiento = self.asientos_disponibles.pop(0)
            print(f"{nombre_cliente} ha reservado el asiento {asiento}")
        else:
            print(f"Lo siento, {nombre_cliente}. No hay más asientos disponibles")
        self.sem_asientos.release()
        
        
# Crearemos una instancia del teatro con 5 asientos
cine = Reservaciones(num_asientos=5)

# Crear clientes
clientes = ["Cliente-1", "Cliente-2", "Cliente-3", "Cliente-4", "Cliente-5", "Cliente-6"]

# Definir Hilos
hilos = []
for cliente in clientes:
    h = threading.Thread(target=cine.reservar_asiento, args=(cliente,))
    hilos.append(h)
    h.start()
    
# Esperar a que termine su ejecución
for h in hilos:
    h.join()
    
# Corroborar que no se puede hacer un release adicional
try:
    cine.sem_asientos.release()
except Exception as error:
    print("\n" + str(error))
    
# Recordatorio:
#   - Los Semáforos son útiles para sincronizar el acceso a recursos compartidos entre múltiples Hilos,
#     evitando condiciones de carrera y asegurando la coherencia en la ejecución de nuestro programa concurrente.
#   - Proporcionan una herramienta eficaz para controlar el acceso a recursos compartidos, como bases de datos,
#     archivos o servicios, garantizando que solo un conjunto de Hilos pueda modificar esos recursos en un momento dado.
