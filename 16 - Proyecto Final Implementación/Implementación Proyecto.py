# Importar librerías
import threading
import multiprocessing
import numpy as np
import time
import os
from estrategia import Crypto_Estrategia


# Instrumentos a analizar (Criptomonedas)
num_instrumentos = 100


# Definir Funciones
def obtener_datos_historicos(clase_estrategia, instrumento, lock, barrera, diccionario, colaFIFO) -> None:
    
    """
    Obtiene datos históricos para un instrumento dentro de una aplicación paralela. Esta función se encarga 
    de sincronizar tanto la descarga de datos y el almacenamiento en objetos de memoria compartida como la 
    comunicación con distintos procesos para realizar el análisis pertinente.
    """
    
    # Obtener datos
    datos = clase_estrategia.obtener_datos(instrumento=instrumento)
    # Guardar en diccionario
    lock.acquire()
    diccionario[instrumento] = datos
    # Tenemos que encolarlo
    colaFIFO.put([instrumento, datos])
    lock.release()
    # Esperar a que terminen para continuar con ejecución
    barrera.wait()
    

def guardar_datos(diccionario, directorio="datos") -> None:
    
    """
    Guarda los datos en un directorio
    """
    
    # Crear una carpeta si no existe
    if not os.path.isdir(directorio):
        os.mkdir(directorio)
    for i in diccionario:
        ruta = os.path.join(directorio, i + ".csv") # Ejemplo: datos/BTCUSDT.csv
        diccionario[i].to_csv(ruta)
        

def obtener_datos_paralelizado(colaFIFO) -> None:
    
    """
    Paraleliza la obtención de datos
    """
    
    # Instanciar clase
    ce = Crypto_Estrategia()
    # Elegir 100 instrumentos
    ce.obtener_activos()
    instrumentos_seleecionados = np.random.choice(ce.instrumentos_financieros, size=num_instrumentos, replace=False)
    # Crear objetos
    lock = multiprocessing.Lock()
    diccionario = multiprocessing.Manager().dict()
    barrera = multiprocessing.Barrier(parties=num_instrumentos + 1, action=lambda: guardar_datos(diccionario))
    for i in range(num_instrumentos):
        t = threading.Thread(target=obtener_datos_historicos, args=(ce, instrumentos_seleecionados[i], lock,
                                                                    barrera, diccionario, colaFIFO))
        # Dormir para que el servidor no nos bloquee
        time.sleep(0.1)
        t.start()
    # Esperar a que todos terminen
    barrera.wait()
    

def detectar_señales(clase_estrategia, colaFIFO, lista_posiciones, lock) -> None:
    
    """
    Analizará si existen oportunidades de inversión
    """
    
    # Esperar a recibir los datos
    while True:
        # Obtener datos históricos que estén en cola
        instrumentos_datos = colaFIFO.get()
        # Revisar si cesar la ejecución
        if instrumentos_datos is None:
            break
        # Desempaquetar
        instrumento, datos = instrumentos_datos
        estrategia = clase_estrategia.Cruce_MA(df=datos)
        # Revisar si hay una señal positiva y que no exista ninguna señal negativa en los últimos 15 minutos
        if ((estrategia["Cruce"][-15:] == 1).sum() > 0) & ((estrategia["Cruce"][-15:] == -1).sum() == 0):
            lock.acquire()
            lista_posiciones.append([instrumento, "Compra"])
            lock.release()
            

if __name__ == "__main__":
    # Establecer Método
    multiprocessing.set_start_method("spawn")
    # Crear objetos
    ce = Crypto_Estrategia()
    colaF = multiprocessing.Queue()
    lista_pos = multiprocessing.Manager().list()
    lock = multiprocessing.Lock()
    # Inicializar Procesos (4 Distintos para realizar cálculos matemáticos)
    procesos = []
    for i in range(4):
        p = multiprocessing.Process(target=detectar_señales, args=(ce, colaF, lista_pos, lock))
        procesos.append(p)
        p.start() # Estarán dormidos hasta que reciban los datos
    # Obtener datos
    obtener_datos_paralelizado(colaFIFO=colaF)
    # Cesar ejecución
    for i in range(4):
        colaF.put(None)
    # Join
    for p in procesos:
        p.join()
    # Imprimir por pantalla las señales de inversión que se encontraron
    print("Posiciones de inversión encontradas:", lista_pos[:])
    
# Recordatorio:
#   - Existirán situaciones donde paralelizar nuestro código no tenga una ventaja en términos de tiempo de ejecución, pero a medida
#     que el proyecto crece y se escala la ventaja será muy notoria.
#   - Un proyecto puede crecer en términos de complejidad a medida que incorporamos más objetos concurrentes.
    