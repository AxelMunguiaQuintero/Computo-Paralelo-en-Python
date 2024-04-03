# Importar librerías
import threading
import time
import queue


# Definir función
def empleado(nombre: str) -> None:
    
    """
    Simular el trabajo diario de un empleado
    """
    
    print(f"{nombre} ha llegado al trabajo")
    
    while True:
        # El empleado toma una tarea de la cola
        tarea = cola_tareas.get()
        # Validar
        if tarea is None:
            break # Si no hay más tareas disponibles, el empleado termine su jornada
        print(f"{nombre} está trabajando en la tarea: {tarea}")
        time.sleep(3)
        print(f"{nombre} ha terminado la tarea: {tarea}")
        
    print(f"{nombre} ha terminado su jornada de trabajo")
            
    
# Definir Queue
cola_tareas = queue.SimpleQueue()

hilos = []
# Simular 3 empleados
for i in range(3):
    t = threading.Thread(target=empleado, args=(f"Trabajador-{i}", ))
    hilos.append(t)
    t.start()

# Definir las tareas que se asignarán
tareas_asignadas = ["Realizar informe", "Enviar correos", "Revisar documentos", "Actualizar proyectos",
                    "Investigar nuevas tecnlogías", "Orgnizar reunión de equipos"]
for tarea in tareas_asignadas:
    cola_tareas.put(tarea)
    
# Cesar la ejecución
for hilo in hilos:
    cola_tareas.put(None)
    hilo.join()
    
print("¡La jornada laboral ha terminado!")

# Recordatorio:
#   - Los Bloqueos Mutuos o Deadlocks pueden ser muy difíciles de detectar en algunas situaciones. Una correcta estructura
#     de código puede ayudar a minimizar la probabilidad de que eso suceda, pero habrá situaciones donde nuestro código corra
#     sin ningún inconveniente y posteriormente encontremos el problema. 
    