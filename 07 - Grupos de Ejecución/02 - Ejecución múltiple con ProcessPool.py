# Importar librerí­as
from concurrent.futures import ProcessPoolExecutor


# Definir función
def suma_cuadrados(rango: tuple) -> int:
    
    """
    Función que calcula la suma de los cuadrados en el rango especificado.
    
    Parámetros
    ----------
    param : tuple : rango : Contiene limite inferior como limite superior.
    ----------
    Salida
    ----------
    return : int : valor : La suma total de los valores en el rango al cuadrado.    
    """
    
    # Calcular
    valor = 0
    for i in range(rango[0], rango[1] + 1):
        valor += i**2
        
    return valor


# Ejecutar
if __name__ == "__main__":
    # Establecer lí­mites
    limites_inferiores = range(0, 10_000, 100) # 100 particiones distintas
    limites_superiores = range(100, 10_100, 100) # 100 particiones distintas
    # Crear rango
    rango = list(zip(limites_inferiores, limites_superiores))
    # Inicializamos Conjunto de Trabajadores
    ppe = ProcessPoolExecutor(max_workers=4)
    
    # Utilizar submit
    cuadrados_submit = [ppe.submit(suma_cuadrados, i) for i in rango]
    # Obtener el resultado (similar a .join en Procesos)
    cuadrados_submit = [i.result() for i in cuadrados_submit]
    print(cuadrados_submit)
    
    # Utilizando map
    cuadrados_map = ppe.map(suma_cuadrados, rango)
    cuadrados_map = [i for i in cuadrados_map]
    print(cuadrados_map)
    
    # Recordatorio:
    #   - Los grupos de ejecución son una herramienta que se encargará de realizar una lista de tareas.
    #   - Son convenientes, pues evitan la creación y destrucción de Procesos y esto mejora la eficiencia de nuestra aplicación.
