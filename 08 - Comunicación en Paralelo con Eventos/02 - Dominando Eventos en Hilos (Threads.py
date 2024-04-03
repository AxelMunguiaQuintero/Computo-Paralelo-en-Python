# Importar librerías
import threading
import time


# Definir Clase
class Adquisicion:
    
    """
    Simular la adquisición de un vehículo
    """
    
    def __init__(self) -> None:
        
        """
        Constructor
        """
        
        # Atributos
        self.costo = 10_000 # Unidades
        self.ingreso_semanal = 500
        self.gastos_semanal = 300 # Ahorro de 200 semanal
        self.ahorros = 0
        self.semanas_transcurridas = 0 # Se necesitarán 50 semanas (50 x 200 = 10_000)
        # Evento 
        self.event = threading.Event()
        
    
    def generar_ingreso(self) -> None:
        
        """
        Función que simula el ingreso que se obtiene de un trabajador        
        """
        
        # Iterador
        while True:
            # Determinar capacidad de ahorro (Ingreso - Gastos)
            ahorros_netos = self.ingreso_semanal - self.gastos_semanal
            self.ahorros += ahorros_netos
            self.semanas_transcurridas += 1
            # Revisar si ya podemos comprar el vehículo
            if self.ahorros >= self.costo:
                print("Dinero ahorrado hasta el momento:", self.ahorros)
                # Cambiaremos el estado interno del evento
                self.event.set()
                break
            # Dormir entre cada iteración
            time.sleep(0.75)
            
        
    def revisar(self) -> None:
        
        """
        Función monitorea el estado intermedio de nuestro trabajador
        """
        
        while True:
            if self.ahorros >= self.costo:
                print("El vehículo ya se puede comprar")
                # Limpiar el estado de la bandera al inicial
                self.event.clear()
                break
            else:
                print("Dinero ahorrado hasta el momento:", self.ahorros)
                # Esperar solo 2 segundos para poder revisar de nuevo
                self.event.wait(timeout=2) # None es cuando queremos esperar hasta que el estado de la bandera cambie
                
                
# Clase
adq = Adquisicion()
t0 = threading.Thread(target=adq.generar_ingreso)
t1 = threading.Thread(target=adq.revisar)
t0.start()
t1.start()
# join
t1.join()
print("Semanas transcurridas:", adq.semanas_transcurridas)
print("Ahorros:", adq.ahorros)
print("Estado de la bandera:", adq.event.is_set())
print("Estado Hilo 0:", t0.is_alive())
print("Estado Hilo 1:", t1.is_alive())

# Recordatorio:
#   - Los Eventos son herramientas que nos ayudan a tener una comunicación simple entre distintos Hilos y
#     nos señalan el cumplimiento de distintas tareas u objetivos.
        