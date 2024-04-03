# Importar librerías
import multiprocessing
import time


# Definir función
def imprimir_documento(sem, documento: str) -> None:
    
    """
    Simular la impresión de un documento
    """
    
    sem.acquire()
    print(f"Una impresora está imprimiendo el documento {documento}")
    time.sleep(2)
    print("La impresora ha terminado de imprimir el documento:", documento)
    sem.release()
    
    
if __name__ == "__main__":
    
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Número de impresoras disponibles
    impresoras = 3
    # Crear semáforo
    sem = multiprocessing.BoundedSemaphore(value=impresoras)
    # Documentos que se imprimirán
    documentos = ["legales", "contratos", "renuncias", "contrataciones", "confidenciales"]
    # Representar la impresión de cada documento como un Proceso
    procesos = []
    for i in range(len(documentos)):
        p = multiprocessing.Process(target=imprimir_documento, args=(sem, documentos[i]))
        procesos.append(p)
        p.start()
    # Esperar a que terminen su ejecución
    for p in procesos:
        p.join()
    # Corroborar un release adicional
    try:
        sem.release()
    except Exception as error:
        print("\n" + str(error))
        
    # Recordatorio:
    #   - Los Semáforos son útiles para sincronizar el acceso a recursos compartidos entre múltiples Procesos.
    #   - Proporcionan una herramienta eficaz para controlar el acceso a recursos compartidos, como bases de datos,
    #     archivos o servicios, garantizando que solo un conjunto de Procesos pueda modificar esos recursos en un momento dado.
        