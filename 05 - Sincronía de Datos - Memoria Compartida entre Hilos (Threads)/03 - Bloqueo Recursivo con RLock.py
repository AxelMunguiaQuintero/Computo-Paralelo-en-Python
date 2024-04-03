# Importar librerías
import threading


# Definir Sincronizadores
# mutex = threading.Lock()
mutex = threading.RLock()


# Definir funciones
def fichero() -> None:
    
    """
    Función se encarga de escribir sobre un documento
    """
    
    # Modificación
    mutex.acquire()
    with open("archivo.txt", "w") as documento:
        documento.write("Función fichero")
        documento.close()
    mutex.release()
    
    
def aplicar_cambios() -> None:
    
    """
    Función que llama a nuestra función fichero
    """
    
    # Adquirir el sincronizador
    mutex.acquire()
    fichero()
    mutex.release()
    
    
# Ejecutar función
aplicar_cambios()
    
# Recordatorio:
#   - El sincronizador recursivo (RLock) nos permite adquirir múltiples veces nuestro sincronizador dentro del mismo Hilo.
#     Este puede llegar a ser ligeramente más lento, pero nos ayuda a evitar puntos muertos de bloqueo. 
