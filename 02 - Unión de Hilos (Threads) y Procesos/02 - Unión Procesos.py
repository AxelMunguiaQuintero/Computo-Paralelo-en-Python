# Importar librerías
import multiprocessing
import psutil # Nos ayuda a conocer el número de núcleos que tiene nuestra computadora

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
    # Establecer límites
    limites_inferiores = range(0, 10_000, 100) # 100 particiones distintas
    limites_superiores = range(100, 10_100, 100) # 100 particiones distintas
    # Número máximo de Procesos en paralelo
    max_procesos = psutil.cpu_count(logical=False)
    lista_procesos = []
    for i in range(len(limites_inferiores)):
        p = multiprocessing.Process(target=suma_cuadrados, args=(limites_inferiores[i], limites_superiores[i]))
        lista_procesos.append(p)
        p.start()
        # Unir Procesos y utilizar el número máximo de núcleos que tenemos
        if len(lista_procesos) == max_procesos:
            # Esperar a que terminen 
            for proc in lista_procesos:
                proc.join()
            # Reiniciar lista
            lista_procesos = []
    # Esperar a que terminen los últimos (4 restantes)
    for proc in lista_procesos:
        proc.join()
    print("Programa ha finalizado")
    
    # Recordatorio:
    #   - JOIN nos permite esperar a que un Proceso termine su ejecución antes de continuar con el resto de la 
    #     ejecución del Programa.
    #   - Debe de existir una gestión de recursos eficiente para no colapsar nuestro sistema.
