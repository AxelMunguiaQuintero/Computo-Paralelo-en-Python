# Importar librerías
import multiprocessing
import time


# Definir clase 
class Adquisicion:
    
    """
    Simular la compra de un vehículo por 2 trabajadores
    """
    
    def __init__(self) -> None:
        
        """
        Constructor
        """
        
        # Atributos
        self.costo = 10_000 # Unidades
        self.ingreso_semanal = 500 # Ambos trabajadores ganan lo mismo
        self.gasto_semanal = 300 # Ambos trabajadores gastan lo mismo
        self.ahorros = multiprocessing.Value("f", 0)
        # Sincronizador
        self.mutex = multiprocessing.Lock()
        # Evento
        self.event = multiprocessing.Event()
        
    
    def trabajador1(self) -> None:
        
        """
        Simula el ingreso que genera un trabajador
        """
        
        # Iterador
        while True:
            # Ahorro neto semanal
            ahorro_neto = self.ingreso_semanal - self.gasto_semanal
            self.mutex.acquire()
            self.ahorros.value += ahorro_neto
            self.mutex.release()
            if self.ahorros.value >= self.costo:
                print("Dinero ahorrado hasta el momento:", self.ahorros.value)
                # Cambiar el estado interno del evento
                self.event.set()
                break
            # Dormir por un momento
            time.sleep(0.75)
            
        
    def trabajador2(self) -> None:
        
        """
        Simula el ingreso que genera un trabajador
        """
        
        # Iterador
        while True:
            # Determinamos el ahorro neto semanal            
            ahorro_neto = self.ingreso_semanal - self.gasto_semanal
            self.mutex.acquire()
            self.ahorros.value += ahorro_neto
            self.mutex.release()
            if self.event.is_set():
                # Limpiar bandera al estado inicial
                self.event.clear()
                break
            # Dormir por un momento
            time.sleep(0.75)
            
            
    def revisar(self) -> None:
        
        """
        Monitorear el nivel de ahorro de ambos trabajadores
        """
        
        while True:
            if self.ahorros.value >= self.costo:
                print("El vehículo ya se puede comprar")
                break
            else:
                print("Dinero ahorrado hasta el momento:", self.ahorros.value)
                self.event.wait(timeout=2)
                
                
if __name__ == "__main__":
    # Método
    multiprocessing.set_start_method("spawn")
    # Inicializar
    adq = Adquisicion()
    p1 = multiprocessing.Process(target=adq.trabajador1)
    p2 = multiprocessing.Process(target=adq.trabajador2)
    p3 = multiprocessing.Process(target=adq.revisar)
    p1.start()
    p2.start()
    p3.start()
    # Join
    p2.join()
    p3.join()
    
    # Información
    print("Ahorros:", adq.ahorros.value)
    print("Estado Bandera:", adq.event.is_set())
    print("Estado Proceso 1:", p1.is_alive())
    print("Estado Proceso 2:", p2.is_alive())
    print("Estado Proceso 3:", p3.is_alive())
    
    # Recordatorio:
    #   - Los Eventos son herramientas que ayudan a tener una comunicación simple entre distintos Procesos y señalan el cumplimiento
    #     de distintas tareas u objetivos.
    #   - Hay más factores que tomar en cuenta en Procesos como los objetos de memoria compartida.
        