# Importar librerías
import multiprocessing
import time


# Definir función
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
        
        
if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Inicializar
    p = multiprocessing.Process(target=func, args=[1])
    p.start()
    # Esperar
    time.sleep(10)
    # Finalizar
    p.kill()
    print("Programa ha finalizado")
    
    # Recordatorio:
    #   - Finalizar programas de manera forzada debería ser nuestra última opción, pues puede conllevar a pérdida de información
    #     o al error de nuestra aplicación.
    #   - Si bien una finalización forzada puede conducir a una ejecución más eficiente (por ejemplo, liberar recursos), esta 
    #     debe estar bien estructurada.
    