# Importar librerías
import multiprocessing


# Definir funciones
def fichero(mutex: multiprocessing.RLock) -> None:
    
    """
    Función se encarga de escribir sobre un documento
    """
    
    # Modificación
    mutex.acquire()
    with open("archivo.txt", "w") as documento:
        documento.write("Función fichero")
        documento.close()
    mutex.release()
    
    
def aplicar_cambios(mutex: multiprocessing.RLock) -> None:
    
    """
    Función que llama a nuestra función fichero
    """
    
    # Adquirir el sincronizador
    mutex.acquire()
    fichero(mutex)
    mutex.release()


if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Definir sincronizador
    mutex = multiprocessing.RLock()
    # Inicializar 
    p = multiprocessing.Process(target=aplicar_cambios, args=(mutex, ))
    p.start()
    p.join()
    
    # Recordatorio:
    #   - El sincronizador recursivo (RLock) nos permite adquirir múltiples veces nuestro sincronizador dentro del mismo
    #     Proceso. Esto puede llegar a ser ligeramente más lento, pero nos ayuda a evitar puntos muertos de bloqueo.
    #   - El mismo número de veces que se adquiere el sincronizador es el mismo número de veces que debe de ser liberado.
