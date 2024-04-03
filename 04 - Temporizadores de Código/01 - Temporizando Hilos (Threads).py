# Importar librerías
import threading
import datetime


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
            
# Calcular tiempo actual
tiempo_actual = datetime.datetime.now()
# Tiempo futuro
tiempo_futuro = tiempo_actual + datetime.timedelta(seconds=60)
# Crear instancia
aut = Automatizacion(fecha_futura=tiempo_futuro)
intervalo = aut.tiempo().seconds
print("El correo se mandará en {} segundos".format(intervalo))
# Inicializar Temporizador
t = threading.Timer(interval=intervalo, function=aut.enviar_correo, args=())
t.start()

# Recordatorio:
#   - Los temporizadores son útiles para actividades que se deben ejecutar en un tiempo futuro y en muchas ocasiones
#     de manera periódica.
