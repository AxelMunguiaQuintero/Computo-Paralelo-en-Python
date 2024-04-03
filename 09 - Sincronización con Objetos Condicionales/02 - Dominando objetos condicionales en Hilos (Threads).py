# Importar librerías
import threading 


# Definir clase
class Empresa:
    
    """
    Clase que genera el comportamiento de ventas y costos de una empresa
    """
    
    def __init__(self, inicial: float = 1_000.00) -> None:
        
        """
        Constructor.
        
        Parámetros
        ----------
        param : float : inicial : Dinero inicial que tiene la empresa (por defecto, 1000 está configurado).
        ----------
        Salida
        ----------
        return : NoneType : None
        """
        
        # Inicializar variables
        self.dinero_t0 = inicial
        self.inicial = inicial # Dinero inicial
        self.mutex = threading.Lock()
        self.cv = threading.Condition(lock=self.mutex)
        
    
    def ventas(self) -> None:
        
        """
        Función de ventas
        """
        
        # Simular 1_000_000
        ingreso = 10
        for i in range(1_000_000):
            # Adquirir Sincronizador
            self.cv.acquire()
            # Acumular ingreso
            self.inicial += ingreso
            self.cv.notify()
            # Liberar Sincronizador
            self.cv.release()
        # Mensaje 
        print("Ventas ha finalizado")
        
        
    def costos(self) -> None:
        
        """
        Función de costos
        """
        
        # Simular 1_000_000
        costo = 10
        for i in range(1_000_000):
            # Adquirir Sincronizador
            self.cv.acquire()
            # Dado que no podemos restar costos si no hay ventas, entonces esperamos
            if self.inicial <= self.dinero_t0:
                self.cv.wait() # Esperar hasta que se realicen más ventas
            self.inicial -= costo
            # Liberar Sincronizador
            self.cv.release()
        # Mensaje
        print("Costos ha finalizado")
        
        
# Instanciar clase
emp = Empresa()
# Hilos 
t1 = threading.Thread(target=emp.ventas)
t2 = threading.Thread(target=emp.costos)
t1.start()
t2.start()
t1.join()
t2.join()

# Calcular el Valor Esperado
inicial = 1_000
ingreso = 10
costo = 10
simulaciones = 1_000_000
valor_esperado = inicial + ingreso * simulaciones - costo * simulaciones # 1_000 Unidades

print("Valor Esperado =", valor_esperado)
print("Valor Final =", emp.inicial)

# Recordatorio:
#   - Los objetos condicionales son herramientas más poderosas que los Eventos.
#   - Se utilizan para la coordinación basada en condiciones específicas.
#   - Podemos notificar a un Hilo o múltiples de que una condición se ha cumplido.
