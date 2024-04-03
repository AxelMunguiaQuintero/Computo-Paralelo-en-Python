# Importar librerías
import multiprocessing
import pandas as pd


if __name__ == "__main__":
    
    # Valor Numérico
    valor_compartido = multiprocessing.Value("i", 0) # Pasar tipo de datos y longitud
    print(valor_compartido.value)
    valor_compartido.value = 10
    print(valor_compartido.value)
    # Arreglo
    array_compartido = multiprocessing.Array("f", [0, 0, 0, 0])
    print(array_compartido[:])
    # Arreglo Dimensional (3x4)
    array_dimensional = [multiprocessing.Array("i", [i, i, i, i]) for i in range(3)]
    for i in array_dimensional:
        print(i[:])
        
    # Manager (Contiene listas y diccionarios)
    manager = multiprocessing.Manager()
    # Lista
    lista_compartida = manager.list([1, 2.0, "Cadena de texto"])
    print(lista_compartida[:])
    lista_compartida[0] = 10
    print(lista_compartida[:])
    # Diccionario
    diccionario_compartido = manager.dict({"DataFrame": pd.DataFrame([1, 2, 3]), "lista": lista_compartida})
    print(diccionario_compartido.items())
    
    # Recordatorio:
    #   - Los objetos de memoria compartida garantizan la integridad de los datos y un orden de ejecución.
    #   - El acceso a objetos de memoria compartida entre Procesos puede llegar a relentizar nuestro código.
