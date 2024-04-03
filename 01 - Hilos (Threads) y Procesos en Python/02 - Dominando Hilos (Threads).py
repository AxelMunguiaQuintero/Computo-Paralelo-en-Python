# Importar librerías
import threading 
import matplotlib.pyplot as plt
import time


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
        self.inicial = inicial # Dinero inicial
        self.historial = [] # Historial de ventas y costos
        
    
    def ventas(self) -> None:
        
        """
        Función de ventas
        """
        
        # Simular 1_000_000
        ingreso = 10
        for i in range(1_000_000):
            # Acumular ingreso
            self.inicial += ingreso
            self.historial.append(1)
        # Mensaje 
        print("Ventas ha finalizado")
        
        
    def costos(self) -> None:
        
        """
        Función de costos
        """
        
        # Simular 1_000_000
        costo = 10
        for i in range(1_000_000):
            self.inicial -= costo
            self.historial.append(-1)
        # Mensaje
        print("Costos ha finalizado")
        
        
# Instanciar clase
emp = Empresa()
# Hilos 
threading.Thread(target=emp.ventas).start()
threading.Thread(target=emp.costos).start()
time.sleep(1)


# Calcular el Valor Esperado
inicial = 1_000
ingreso = 10
costo = 10
simulaciones = 1_000_000
valor_esperado = inicial + ingreso * simulaciones - costo * simulaciones # 1_000 Unidades

print("Valor Esperado =", valor_esperado)
print("Valor Final =", emp.inicial)

# Competencia por Intérprete Global
plt.figure(figsize = (12, 6))
plt.plot(emp.historial)
plt.title("Compentencia por el Intérprete Global")
plt.show()

# Recordatorio:
#   - Los Hilos son útiles para problemas de Entrada/Salida. Por otro lado, cuando nuestro código requiere de efiencia
#     computacional eso puede ocasionar un problema donde cada Hilo lucha por obtener el Bloqueo del Intérprete Global.
#   - Cada Hilo dentro de un proceso comparte el mismo espacio de memoria, lo que significa que pueden acceder y modificar
#     las mismas variables y datos. Sin el uso adecuado de técnicas de sincronización, nuestro código puede obtener resultados
#     no concluyentes. Las técnicas de sincronización las veremos más adelante.    
            