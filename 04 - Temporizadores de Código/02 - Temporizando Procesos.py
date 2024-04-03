# Importar librerías
import multiprocessing
import datetime
import time


# Definir clase
class Automatizacion:
    
    """
    Clase que nos ayudará a automatizar actividades diarias del trabajo.
    """
    
    # Constructor
    def __init__(self, fecha_futura: datetime.datetime) -> None:
        
        """
        Constructor
        
        Parámetros
        ----------
        param : datetime.datetime : fecha_futura : Hora a la que se mandará nuestro correo.
        ----------
        Salida
        ----------
        return : NoneType : None.
        """
        
        # Atributos
        self.fecha_futura = fecha_futura
        
    
    def enviar_correo(self) -> None:
        
        """
        Simula el envío de un correo.
        """
        
        # Enviar el correo
        ...
        print("Información enviada")
        
        
    def tiempo(self) -> datetime.datetime:
        
        """
        Calcula el tiempo restante para enviar el correo
        """
        
        # Revisar tiempo actual
        actual = datetime.datetime.now()
        # Tiempo de envío
        tiempo_envio = self.fecha_futura
        # Revisar si no se ha excedido el tiempo
        if not (actual > tiempo_envio):
            diferencia = tiempo_envio - actual
            return diferencia
        else:
            raise ValueError("El tiempo proporcionado es en tiempo pasado.")
            
            
# Timer/Temporizador
def timer(aut, segundos: float) -> None:

    time.sleep(segundos)
    aut.enviar_correo()
    
    
if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Calcular tiempo
    tiempo_actual = datetime.datetime.now()
    # Fecha futura (+2 minutos)
    tiempo_futuro = tiempo_actual + datetime.timedelta(seconds=120)
    # Instanciar clase
    aut = Automatizacion(fecha_futura=tiempo_futuro)
    intervalo = aut.tiempo().seconds
    print("El correo se mandará en {} segundos".format(intervalo))
    # Definir e inicializar el Proceso
    p = multiprocessing.Process(target=timer, args=(aut, intervalo))
    p.start()
    
    # Recordatorio:
    #   - Los temporizadores son útiles para actividades que se deben de ejecutar en un tiempo futuro.
    #   - Los temporizadores están únicamente implentados de manera nativa para los Hilos. No es particularmente eficiente
    #     utilizar todo el poder de un Proceso para mantenerlo en espera. Las tareas que requieren un tiempo de espera
    #     son ejecutadas en Hilos y no Procesos.
