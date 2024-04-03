# Importar librerías
import multiprocessing
import time


# Definir función
def estudiante(nombre, cola_tareas) -> None:
    
    """
    Simular a un estudiante realizando tareas
    """
    
    while True:
        tarea = cola_tareas.get()
        if tarea is None:
            cola_tareas.task_done()
            break
        print(f"{nombre} está trabajando en la tarea: {tarea}")
        time.sleep(2)
        print(f"{nombre} ha terminado la tarea: {tarea}")
        # Indicar que la tarea ha sido completado
        cola_tareas.task_done()
    
    print(f"{nombre} ha terminado su día de clases")
    
    
if __name__ == "__main__":
    
    # Método
    multiprocessing.set_start_method("spawn")
    # Inicializar Cola
    cola_joinable = multiprocessing.JoinableQueue()
    
    # Crear procesos
    estudiantes = ["María", "Juan", "Sofía"]
    procesos_estudiantes = [multiprocessing.Process(target=estudiante, args=(nombre, cola_joinable)) for nombre in estudiantes]
    
    # Inicializar a cada Proceso
    for p in procesos_estudiantes:
        p.start()
        
    # Encolar tareas
    tareas = ["Hacer ejercicios de matemáticas", "Redactar un ensayo", "Investigar un tema de ciencia"]
    for tarea in tareas:
        cola_joinable.put(tarea)
        
    # Cesar la ejecución
    for i in range(len(procesos_estudiantes)):
        cola_joinable.put(None)
        
    # Bloquearemos a nuestra cola hasta que todas las tareas se terminen
    cola_joinable.join()
    
    print("Todos los estudiantes han terminado sus tareas")
        
    # Recordatorio:
    #   - La Cola de Unión permite esperar a que cada una de las tareas se hubiese realizado. Somos quienes deben de indicar cuando
    #     una tarea ha sido completada para que el contador interno se decremento hasta llegar a cero.
