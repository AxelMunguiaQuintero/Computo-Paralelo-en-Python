# Importar librerías
import threading
import time


# Funciones
def func1(segundos: float) -> None:
    
    """
    Función que ejecutará el primer Hilo.
    
    Parámetros
    ----------
    param : float : segundos : Segundos que nuestro programa dormirá entre cada iteración
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
    Función que ejecutará el segundo Hilo.
    
    Parámetros
    ----------
    param : float : segundos : Segundos que nuestro programa dormirá entre cada iteración
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
t1 = threading.Thread(target=func1, args=[1], daemon=True)
t2 = threading.Thread(target=func2, args=[1], daemon=True)
# Inicializar Hilos
t1.start()
t2.start()

# Dormir
time.sleep(8)
print("Finalizar Programa")

# Recordatorio:
#   - Los Hilos Daemon se cierran tan pronto el programa termina de ejecutarse. Esto puede llevar a una pérdida de información
#     si dicho Hilo no había terminado su ejecución.
