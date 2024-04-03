# Importar librerías
import multiprocessing


# Definir funciones
def modificar_valor(valor: int, objeto_compartido: multiprocessing.Value, mutex: multiprocessing.Lock) -> None:
    
    """
    Modifica el valor de un objeto de memoria compartida.
    
    Parámetros
    ----------
    param : int : valor : Un valor que se agregará al objeto de memoria compartida.
    ----------
    param : multiprocessing.Value : objeto_compartido : Objeto de memoria compartida.
    ----------
    param : multiprocessing.Lock : mutex : Sincronizador.
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Modificar
    mutex.acquire()
    objeto_compartido.value += valor
    mutex.release()
    
def modificar_array(valor: int, idx: int, objeto_compartido: multiprocessing.Value, mutex: multiprocessing.Lock) -> None:
    
    """
    Modifica el valor de un objeto de memoria compartida.
    
    Parámetros
    ----------
    param : int : valor : Un valor que se agregará al objeto de memoria compartida.
    ----------
    param : int : idx : Índice donde el valor se modificará.
    ----------
    param : multiprocessing.Value : objeto_compartido : Objeto de memoria compartida.
    ----------
    param : multiprocessing.Lock : mutex : Sincronizador.
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Modificar
    mutex.acquire()
    objeto_compartido[idx] = valor
    mutex.release()
    
def modificar_lista(valor: int, idx: int, objeto_compartido: multiprocessing.Value, mutex: multiprocessing.Lock) -> None:
        
        """
        Modifica el valor de un objeto de memoria compartida.
        
        Parámetros
        ----------
        param : int : valor : Un valor que se agregará al objeto de memoria compartida.
        ----------
        param : int : idx : Índice donde el valor se modificará.
        ----------
        param : multiprocessing.Value : objeto_compartido : Objeto de memoria compartida.
        ----------
        param : multiprocessing.Lock : mutex : Sincronizador.
        ----------
        Salida
        ----------
        return : NoneType : None
        """
        
        # Modificar
        mutex.acquire()
        objeto_compartido[idx] = valor
        mutex.release()

def modificar_diccionario(valor: int, clave: int, objeto_compartido: multiprocessing.Value, mutex: multiprocessing.Lock) -> None:
    
    """
    Modifica el valor de un objeto de memoria compartida.
    
    Parámetros
    ----------
    param : int : valor : Un valor que se agregará al objeto de memoria compartida.
    ----------
    param : int : clave : Índice donde el valor se modificará.
    ----------
    param : multiprocessing.Value : objeto_compartido : Objeto de memoria compartida.
    ----------
    param : multiprocessing.Lock : mutex : Sincronizador.
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Modificar
    mutex.acquire()
    objeto_compartido[clave] = valor
    mutex.release() 
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    
    # Definir sincronizador
    mutex = multiprocessing.Lock()
    
    # Modificar valor
    valor_compartido = multiprocessing.Value("i", 0)
    procesos = []
    for i in range(1, 6): # Levantar 5 Procesos
        p = multiprocessing.Process(target=modificar_valor, args=(i, valor_compartido, mutex))
        procesos.append(p)
        p.start()
    # Esperar a que terminen todos
    for proc in procesos:
        proc.join()
    print("El valor final es:", valor_compartido.value)
    
    # Modificar Arreglo
    array_compartido = multiprocessing.Array("i", [0, 0, 0, 0, 0])
    procesos = []
    for i in range(1, 6): # Levantar 5 Procesos
        p = multiprocessing.Process(target=modificar_array, args=(i, i - 1, array_compartido, mutex))
        procesos.append(p)
        p.start()
    # Esperar a que terminen todos
    for proc in procesos:
        proc.join()
    print("Array final es:", array_compartido[:])
        
    # Modificar Lista
    manager = multiprocessing.Manager()
    lista_compartida = manager.list([0, 0, 0, 0, 0])
    procesos = []
    for i in range(1, 6): # Levantar 5 Procesos
        p = multiprocessing.Process(target=modificar_lista, args=(i, i - 1, lista_compartida, mutex))
        procesos.append(p)
        p.start()
    # Esperar a que terminen todos
    for proc in procesos:
        proc.join()
    print("Lista final es:", lista_compartida[:])
    
    # Modificar Diccionario
    diccionario_compartido = manager.dict()
    procesos = []
    for i in range(1, 6): # Levantar 5 Procesos
        p = multiprocessing.Process(target=modificar_diccionario, args=(i, i - 1, diccionario_compartido, mutex))
        procesos.append(p)
        p.start()
    # Esperar a que terminen todos
    for proc in procesos:
        proc.join() 
    print("Diccionario final es:", diccionario_compartido.items())
    
    # Recordatorio:
    #   - Los sincronizadores nos permiten mantener la integridad de los datos.
    #   - Los objetos de memoria compartida son útiles para compartir, agregar o modificar información entre Procesos.
    #   - Los objetos de memoria compartida son más lentos.
