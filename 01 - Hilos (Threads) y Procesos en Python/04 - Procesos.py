# Importar librerías
import multiprocessing


# Definir función
def suma_cuadrados(limite_inferior: int, limite_superior: int) -> None:
    
    """
    Función que calcula la suma de los cuadrados en el límite indicado
    
    
    Parámetros
    ----------
    param : int : limite_inferior : Límite inferior de nuestro rango
    ----------
    param : int : limite_superior : Límite superior de nuestro rango
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Calcular
    valor = 0
    for i in range(limite_inferior, limite_superior + 1):
        valor += i**2
    print(f"Suma de los cuadrados en el rango de {limite_inferior} a {limite_superior} = {valor}")
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Existen 3 métodos para inicializar un proceso:
    #   1. spawn: Crea un nuevo hijo. Es el más utilizado y el estándar en la mayoría de los escenarios.
    #   2. fork: Crea un hijo idéntico al padre. Es usado en sistemas UNIX.
    #   3. forkserver: Utiliza un proceso de servidor para crear nuevos procesos. 
    
    # Establecer límites
    limites_inferiores = [0, 100, 200, 300, 400, 500, 600, 700, 800]
    limites_superiores = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    for i in range(len(limites_inferiores)):
        p = multiprocessing.Process(target=suma_cuadrados, args = (limites_inferiores[i], limites_superiores[i]))
        p.start()
        
    # Recordatorio:
    #   - Los Procesos son especialmente útiles en tareas que requieren eficiencia computacional.
    #   - Un Proceso es una instancia independiente del intérprete de Python que se ejecutará en su propio espacio de memoria.
    #   - A diferencia de los Hilos, los Procesos no están afectados por el Bloqueo del Intérprete Global (GIL), lo que permite
    #     una ejecución verdaramente paralela.
    #   - El límite de los procesadores que deberíamos correr, se debería de limitar a el número de núcleos que nuestra computadora
    #     tiene (si se inicializan más procesos o muchos, nuestro sistema operativo puede empezar a destruir algunos Procesos para
    #     preservar el funcionamiento del sistema).
