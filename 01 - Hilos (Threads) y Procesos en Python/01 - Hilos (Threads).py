# Importar librerías
import threading 
import time


# Definir funciones
def func1(segundos: float) -> None:
    
    """
    Función que ejecutará el Primer Hilo.
    
    Parámetros
    ----------
    param : float : segundos : Segundos que nuestro programa dormirá entre cada iteración.
    ----------
    Salida
    ----------
    return : NoneType : None.
    """
    
    # Ejecutar
    while True:
        print("Hilo No. 1")
        time.sleep(segundos)
        
def func2(segundos: float) -> None:
    
    """
    Función que ejecutará el Segundo Hilo.
    
    Parámetros
    ----------
    param : float : segundos : Segundos que nuestro programa dormirá entre cada iteración.
    ----------
    Salida
    ----------
    return : NoneType : None.
    """
    
    # Ejecutar
    while True:
        print("Hilo No. 2")
        time.sleep(segundos)
        
# Hilos
t1 = threading.Thread(target=func1, args=[3], name="ID:1") # kwargs={"segundos":3}
t2 = threading.Thread(target=func2, args=[3], name="ID:2")
# Inicializar Hilos
t1.start()
t2.start()

# Recordatorio:
#   - Los Hilos se ejecutan dentro de un Proceso, y dentro de un proceso puedes tener uno o más hilos en ejecución.
#   - Cada Hilo dentro de un proceso comparte el mismo espacio de memoria, lo que significa que pueden acceder y modificar
#     las mismas variables y datos.
#   - Se le puede asignar un identificador único a cada Hilo.     
