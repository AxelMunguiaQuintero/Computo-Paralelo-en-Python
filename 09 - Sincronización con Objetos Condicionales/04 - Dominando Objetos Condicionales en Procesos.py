# Importar librerías
import multiprocessing
from sklearn.linear_model import LinearRegression # Crear un Modelo de Regresión Lineal
from sklearn.metrics import r2_score # Calcular la precisión del modelo (Que tan bueno o malo es)
import numpy as np
import matplotlib.pyplot as plt
import json
import time


# Crear 10 muestras de una Distribución Normal
Xs = [np.random.normal(loc=0.0, scale=1.0, size=(100,1)) for i in range(10)] # Variable Independiente
Ys = [Xs[i] + np.random.normal(loc=0.0, scale=1.0, size=(100,1)) / 3 for i in range(10)] # Variable Dependiente

# Observar como se ve cada grupo de datos
fig, axes = plt.subplots(nrows=2, ncols=5, figsize = (12, 12))
# Realizar gráficos
for n, ax in enumerate(axes.flatten()):
    ax.scatter(Xs[n], Ys[n])
plt.show()


def reg_lin(xs, ys, diccionario, claves, condicional, lista) -> None:
    
    """
    Función que ajusta una regresión lineal a cada subconjunto de datos y guarda cada modelo dentro de un diccionario.
    
    Parámetros
    ----------
    param : list : xs : 10 diferentes conjuntos de datos (variables independientes).
    ----------
    param : list : ys : 10 diferentes conjuntos de datos (variables dependientes).
    ----------
    param : multiprocessing.Manager().dict : diccionario : Diccionario de memoria compartida dode guardaremos los modelos y los datos.
    ----------
    param : list : claves : Claves se usarán para guardar cada modelo.
    ----------
    param : multiprocessing.Condition : condicional : Objeto Condicional.
    ----------
    param : multiprocessing.Manager().list : lista : Lista de memoria compartida.
    ----------
    Salida
    ----------
    return: NoneType : None
    """
    
    # Adquirir
    condicional.acquire()
    # Ajustar modelo
    for n, (x, y) in enumerate(zip(xs, ys)):
        # Crear modelo
        modelo = LinearRegression()
        # Entrenar modelo
        modelo.fit(x, y)
        # Guardar en el diccionario
        diccionario[claves[n]] = [x, y, modelo]
        # Guarda clave en lista
        lista.append(claves[n])
        # Dormir
        time.sleep(0.25)
    # Notificar
    condicional.notify() # El oto Proceso calculará la precisión de cada modelo 
    # Ahora esperamos a que termine el otro proceso
    print("Regresión Lineal esta esperando el condicional")
    condicional.wait()
    # Guardar modelos
    guardar_modelos(diccionario)
    # Liberamos el condicional
    condicional.release()
    print("Regresión Lineal ha terminado")
    
    
def precision(diccionario, condicional, lista) -> None:
    
    """
    Función que calcula la precisión del modelo.
    
    Parámetros
    ----------
    param : multiprocessing.Manager().dict : diccionario : Diccionario de memoria compartida dode guardaremos los modelos y los datos.
    ----------
    param : multiprocessing.Condition : condicional : Objeto Condicional.
    ----------
    param : multiprocessing.Manager().list : lista : Lista de memoria compartida.
    ----------
    Salida
    ----------
    return: NoneType : None
    """
    
    # Precisión    
   
    
    # Precisión
    condicional.acquire()
    # Esperar a que todos los modelos estén entrenados
    print("Precision esta esperando a que se libere el condicional")
    condicional.wait()
    for i in lista[:]:
        # Obtenemos modelo y los datos
        x, y, modelo = diccionario[i]
        # Predecir valores
        y_pred = modelo.predict(x)
        # Calcular el coeficiente de determinación (R^2) -> Metrica para medir la efectividad del modelo
        r2 = r2_score(y_true=y, y_pred=y_pred)
        diccionario[i] += [r2]
        time.sleep(0.1)
    # Notificar que se ha terminado al proceso no. 1
    condicional.notify()
    condicional.release()
    print("Precision ha terminado")
        
    
def guardar_modelos(diccionario) -> None:
    
    """
    Guarda los modelos y su información en un archivo.
    
    Parámetros
    ----------
    param : multiprocessing.Manager().dict : diccionario : Diccionario de memoria compartida dode guardaremos los modelos y los datos.
    ----------
    Salida
    ----------
    return: NoneType : None
    """
    
    print("Guardar Modelos")
    modelos = {}
    for i in diccionario.keys():
        modelos[i] = {
            
            "Coeficiente": diccionario[i][2].coef_[0][0],
            "Intercepto": diccionario[i][2].intercept_[0],
            "r2": diccionario[i][3]
            
            }
    # Guardar
    with open("modelos.txt", "w") as modelos_archivo:
        json.dump(modelos, modelos_archivo)
        
    
if __name__ == "__main__":
    
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Crear objetos
    diccionario = multiprocessing.Manager().dict()
    lista = multiprocessing.Manager().list()
    cv = multiprocessing.Condition(lock=multiprocessing.Lock())
    claves = [f"Modelo{i}" for i in range(10)]
    # Inicializar
    p1 = multiprocessing.Process(target=reg_lin, args=(Xs, Ys, diccionario, claves, cv, lista))
    p2 = multiprocessing.Process(target=precision, args=(diccionario, cv, lista))
    p2.start()
    time.sleep(2)
    p1.start()
    # JOIN
    p1.join()
        
    # Recordatorio:
    #   - La interacción entre Procesos con Objetos Condicionales nos permite ejecutar nuestro código de de una manera más sincronizada.
    #   - Los objetos Condicionales son útiles para el cumplimiento de sucesos que ocurren en otras aplicaciones, por lo que permite una
    #     interacción más amplia en nuestros programas concurrentes.
