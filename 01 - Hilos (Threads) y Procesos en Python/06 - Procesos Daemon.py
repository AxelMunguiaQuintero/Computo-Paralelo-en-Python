# Importar librerías
import multiprocessing
import numpy as np
import time


# Definir función
def fibonacci(lista_valores: list, valor_comparativo: float = np.inf) -> None:
    
    """
    Caclula la Sucesión Fibonacci hasta que el valor calculado sea mayor o igaul al valor con el que
    se le compara.
    
    Parámetros
    ----------
    param : list : lista_valores : Lista inicial con valores.
    ----------
    param : float : valor_comparativo : Valor comparativo que sirve para frenar la ejecución del código
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    valor_fibo = 0.0
    while valor_fibo < valor_comparativo:
        valor_fibo = lista_valores[-1] + lista_valores[-2]
        lista_valores.append(valor_fibo)
        print(f"Valor más reciente de la sucesión Fibonacci: {valor_fibo}")
        time.sleep(0.5)
        
        
if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Definir valores para función
    valores_fibonacci = [0, 1]
    # Declarar e inicializar el proceso
    p = multiprocessing.Process(target=fibonacci, args=(valores_fibonacci, np.inf), daemon=True)
    p.start()
    # Dormir 5 segundos
    time.sleep(5)
    print("Programa Finalizado")
    
    
    # Recordatorio:
    #   - Los Procesos Daemon se cierran tan pronto el programa se ha terminado de ejecutar. Esto puede llevar a una pérdida
    #     de información si dicho Proceso no había terminado su ejecución.
