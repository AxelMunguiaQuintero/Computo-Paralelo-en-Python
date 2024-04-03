# Importar librerías
import multiprocessing
import pandas as pd
import numpy as np
import time

# Crear DataFrame de 0s y 1s
serie0 = pd.DataFrame(data=np.random.randint(low=0, high=2, size = (1_000_000, )), columns = ["Serie"])
serie1 = pd.DataFrame(data=np.random.randint(low=0, high=2, size = (1_000_000, )), columns = ["Serie"])


# Definir función
def mantener_subconjunto_secuencial(datos: pd.DataFrame) -> pd.DataFrame:
    
    """
    Devuleve un subconjunto de datos de la serie original, aquellos con valor de 1.
    """
    
    # Iterar
    indices = []
    valores = []
    for i in datos.iterrows():
        # Revisar que sea igual a 1
        if i[1][0] == 1:
            indices.append(i[0])
            valores.append(i[1][0])
        else:
            continue
        
    # Crear DataFrame
    subconjunto = pd.DataFrame(data=valores, index=indices, columns=["Serie"])
    
    return subconjunto


def mantener_subconjunto_paralelo(datos: pd.DataFrame, dict_memoria_compartida: dict, clave: str, lock) -> pd.DataFrame:
    
    """
    Devuleve un subconjunto de datos de la serie original, aquellos con valor de 1.
    """
    
    # Iterar
    indices = []
    valores = []
    for i in datos.iterrows():
        # Revisar que sea igual a 1
        if i[1][0] == 1:
            indices.append(i[0])
            valores.append(i[1][0])
        else:
            continue
        
    # Crear DataFrame
    subconjunto = pd.DataFrame(data=valores, index=indices, columns=["Serie"])
    # Guardarlo en diccionario
    lock.acquire()
    dict_memoria_compartida[clave] = subconjunto
    lock.release()
    

def mantener_subconjunto_optimizado(datos: pd.DataFrame) -> pd.DataFrame:
    
    """
    Devuleve un subconjunto de datos de la serie original, aquellos con valor de 1.
    """
    
    return datos[datos == 1].dropna()


def mantener_subconjunto_optimizado_paralelizado(datos: pd.DataFrame, diccionario, clave, lock) -> pd.DataFrame:
    
    """
    Devuleve un subconjunto de datos de la serie original, aquellos con valor de 1.
    """
    
    lock.acquire()
    diccionario[clave] = datos[datos == 1].dropna()
    lock.release()


# Diseño lógico
valores_log = [False] * 9_900_000 + [True] * 100_000
valores_random = np.random.randint(low=0, high=11, size=(10_000_000,))


# Definir funciones
def estructura_logica_ineficiente(valores_logicos, valores_random) -> None:
    
    """
    Mide el tiempo que se tarda en ejecutar.
    """
    
    # Tomar tiempo
    inicio = time.time()
    valores = []
    for vl, vr in zip(valores_log, valores_random):
        if (vr < 5) & (vl is False):
            continue
        elif (vr > 5) & (vl is True):
            valores.append([vl, vr])
    print("Tamaño:", len(valores))
    print("Tomó {} segundos".format(time.time() - inicio))
    
    
def estructura_logica_poco_eficiente(valores_logicos, valores_random) -> None:
    
    """
    Mide el tiempo que se tarda en ejecutar.
    """
    
    # Tomar tiempo
    inicio = time.time()
    valores = []
    for vl, vr in zip(valores_log, valores_random):
        # Solo el 1% cumple la condición de verdadero. Que compare primero el valor 
        # booleano y si es verdader entonces que revise también el valor
        if vl & (vr > 5):
            valores.append([vl, vr])
    print("Tamaño:", len(valores))
    print("Tomó {} segundos".format(time.time() - inicio))


def estructura_logica_eficiente(valores_logicos, valores_random) -> None:
    
    """
    Mide el tiempo que se tarda en ejecutar.
    """
    
    # Tomar tiempo
    inicio = time.time()
    valores_logicos = np.array(valores_logicos)
    # La multiplicación de valores booleanos es como multiplicar 0s (False) y 1s (True)
    # Nos interesan los que den como resultado 1
    subconjunto = valores_logicos * (valores_random > 5)
    subconjunto = list(zip(valores_logicos[subconjunto], valores_random[subconjunto]))
    print("Tamaño:", len(subconjunto))
    print("Tomó {} segundos".format(time.time() - inicio))


# Ejecutar
if __name__ == "__main__":
    # Método 
    multiprocessing.set_start_method("spawn")
    
    
    # Comparar tiempos
    print("############## Lógica y Diseño ##############")
    
    # Medir tiempo para estructuras lógicas primero
    print("\nEstructura Ineficiente")
    estructura_logica_ineficiente(valores_log, valores_random)
    print("-" * 40)
    print("\nEstructura Poco Eficiente")
    estructura_logica_poco_eficiente(valores_log, valores_random)
    print("-" * 40)
    print("\nEstructura Eficiente")
    estructura_logica_eficiente(valores_log, valores_random)
    print("-" * 40)
    
    print("############## ############### ##############", end="\n"*3)
        
    
    print("############## Vectorización ##############")
    
    print("\nEstructura Ineficiente")
    inicio = time.time()
    mantener_subconjunto_secuencial(serie0)
    mantener_subconjunto_secuencial(serie1)
    print("Tomó {} segundos".format(time.time() - inicio))
    print("-" * 40)
    
    print("\nEstructura eficiente")
    inicio = time.time()
    mantener_subconjunto_optimizado(serie0)
    mantener_subconjunto_optimizado(serie1)
    print("Tomó {} segundos".format(time.time() - inicio))
    print("-" * 40)

    print("\nEstructura Ineficiente Paralelizado")
    inicio = time.time()
    lock = multiprocessing.Lock()
    dicc = multiprocessing.Manager().dict()
    p0 = multiprocessing.Process(target=mantener_subconjunto_paralelo, args=(serie0, dicc, "Serie0", lock))
    p0.start()
    p1 = multiprocessing.Process(target=mantener_subconjunto_paralelo, args=(serie1, dicc, "Serie1", lock))
    p1.start()
    p0.join()
    p1.join()
    print("Tomó {} segundos".format(time.time() - inicio))
    print("-" * 40)
    
    print("\nEstructura Eficiente Paralelizado")
    inicio = time.time()
    lock = multiprocessing.Lock()
    dicc_ef = multiprocessing.Manager().dict()
    p0 = multiprocessing.Process(target=mantener_subconjunto_optimizado_paralelizado, args=(serie0, dicc_ef, "Serie0", lock))
    p0.start()
    p1 = multiprocessing.Process(target=mantener_subconjunto_optimizado_paralelizado, args=(serie1, dicc_ef, "Serie1", lock))
    p1.start()
    p0.join()
    p1.join()
    print("Tomó {} segundos".format(time.time() - inicio))
    print("-" * 40)

    print("############## ############# ##############", end="\n"*3)
    
# Recordatorio:
#   - La mejor manera de optimizar nuestro código y/o aplicación es con una correcta estructura de código.
#   - Los Procesos e Hilos (Threads) son herramientas altamente eficientes para reducir el tiempo de ejecución de nuestra
#     aplicación, pero podemos obtener resultados muy prometedores con un código bien hecho (no siempre).
