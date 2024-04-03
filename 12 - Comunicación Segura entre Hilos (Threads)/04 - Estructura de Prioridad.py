# Importar librerías
import queue
import threading
import time
import random


# Definir funciones
def enfermera() -> None:
    
    """
    Simular la atención de un personal médico
    """
    
    while True:
        urgencia, tarea, solucion = cola_prioridad.get()
        if tarea is None:
            cola_prioridad.task_done()
            break
        print(f"Tarea asignada: {tarea}")
        # Aplicar solución
        solucion(urgencia)
        # Simulamos el tiempo de atencion
        time.sleep(random.randint(a=1, b=4))
        # Tarea completada
        cola_prioridad.task_done()
        
        
def solucionar_emergencia(urgencia: int) -> None:
    
    """
    Simular que la emergencia se ha resuelto
    """
    
    # Urgencia es < 5 es muy grave
    # Urgencia es >= 5 es leve
    if urgencia < 5:
        print("El paciente ha sido operado y está en recuperación...")
    else:
        print("El paciente ha sido recetado con un medicamento...")
        

def paciente(nombre: str) -> None:
    
    """
    Simular la llegada de un paciente con un problema para ser atendido
    """
    
    urgencia = random.randint(a=1, b=11)
    tarea = f"Atender a {nombre} con Urgencia: {urgencia}"
    print("Nueva tarea:", tarea)
    # Mandar los datos a encolar
    cola_prioridad.put((urgencia, tarea, solucionar_emergencia))
    
    
# Definir Cola
cola_prioridad = queue.PriorityQueue(maxsize=0)    
    

# Simular la llegada de Pacientes
pacientes = ["Juan", "Ana", "Carlos", "María", "Luis"]
hilos_pacientes = []
for nombre in pacientes:
    t = threading.Thread(target=paciente, args=(nombre, ))
    hilos_pacientes.append(t)
    t.start()
    
print("\n ----- Segmento Informativo -----\n")
print("Total de objetos en la cola:", cola_prioridad.qsize())
print("Tamaño de nuestra cola:", cola_prioridad.maxsize)
print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_prioridad.empty())
print("Número de tareas restantes =", cola_prioridad.unfinished_tasks)
print("\n ----- -------------------- -----\n")
    
# Crear un Hilo para la enfermera que atiende las tareas
hilo_enfermera = threading.Thread(target=enfermera, args=())
hilo_enfermera.start()

# Indicar que ya no hay más tareas
# Agregar un número muy grande para que sea el último que se atienda
cola_prioridad.put((float("inf"), None, None))

# Join
hilo_enfermera.join()
    
print("\n ----- Segmento Informativo -----\n")
print("Total de objetos en la cola:", cola_prioridad.qsize())
print("Tamaño de nuestra cola:", cola_prioridad.maxsize)
print("¿Está la cola vacía (se han realizado todas las tareas pendientes)?:", cola_prioridad.empty())
print("Número de tareas restantes =", cola_prioridad.unfinished_tasks)
print("\n ----- -------------------- -----\n")

print("¡Ya no hay más pacientes!")
    
# Recordatorio:
#   - Las colas de Prioridad son útiles cuando se debe de seguir un orden de importancia. Cuentan también con 
#     una mayor cantidad de funcionalidades a diferencia de la Cola Simple.
#   - Cada elemento que está dentro de la Cola se ordena en base al orden de importancia que se le asignó.
