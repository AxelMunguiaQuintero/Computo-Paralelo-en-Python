# Importar librerías
import threading
import time
import ctypes


# Definir funciones
def func(segundos: float) -> None:
    
    """
    Función que será finalizada forzadamente
    
    Parámetros
    ----------
    param : float : segundos : Segundos que nuestro programa dormirá entre cada iteración
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Ejecutar
    while True:
        print("Esperando hasta ser finalizado")
        time.sleep(segundos)


def finalizar_hilo(hilo: threading.Thread) -> bool:

    """
    Esta función finalizará un Hilo activo. No se recomienda finalizar un objeto de tipo Thread, ya que puede
    llevar a una pérdida de información. Se debe de tener una buena gestión e implementación para evitar cualquier
    pérdida de datos.
    
    Parámetros
    ----------
    param : threading.Thread : hilo : Hilo que se desea finalizar
    ----------
    Salida
    ----------
    return : bool : True si fue posible finalizar el Hilo o False si no lo fue
    """
    
    # Finalizar
    hilo_id = hilo.native_id
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(hilo_id, ctypes.py_object(SystemExit))
    # Revisar respuesta
    if res > 1:
        
        return True if ctypes.pythonapi.PyThreadState_SetAsyncExc(hilo_id, 0) == 0 else False
    else:
        return True
    
    
# Inicializar Hilo
t = threading.Thread(target=func, args=[1])
t.start()
# Dormir código
time.sleep(10)
print(finalizar_hilo(hilo=t))
print("Programa ha finalizado")
       
# Recordatorio:
#   - Finalizar programas de manera forzada debería ser nuestra última opción, pues puede conllevar a pérdida de información
#     o al error de nuestra aplicación.
#   - Si bien una finalización forzada puede conducir a una ejecución más eficiente (por ejemplo, liberar recursos), esta 
#     debe estar bien estructurada.
