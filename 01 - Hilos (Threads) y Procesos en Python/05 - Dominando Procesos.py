# Importar librerías
import multiprocessing
import os

# Crear documento
archivo = "archivo.txt" # Documento donde los Procesos guardarán 
if not os.path.isfile(archivo):
    documento = open(archivo, "w") 


# Definir función
def guardar_datos(datos: str, nombre_archivo: str) -> None:
    
    """
    Abre un archivo y agrega datos
    
    Parámetros
    ----------
    param : str : datos : Datos que se agregarán e imprimirán por consola
    ----------
    param : str : nombre_archivo : Nombre del archivo donde se agregarán los datos o información
    ----------
    Salida
    ----------
    return : NoneType : None
    """
    
    # Agregar el contenido
    with open(archivo, "a") as documento_func:
        documento_func.write(datos)
        documento_func.write("\n")
        documento_func.close()
    print(f"Finalizando con datos: {datos}")
    

if __name__ == "__main__":
    # Establecer método
    multiprocessing.set_start_method("spawn")
    # Inicializar 4 Procesos
    for i in range(4):
        p = multiprocessing.Process(target=guardar_datos, name=f"Proceso_{i}", args=(f"Proceso_{i}", archivo))
        p.start()
        

# Recordatorio:
#   - Cada Proceso realizará una clonación de recursos para poder ejecutarse de manera correcta. Es importante
#     estructurar nuestro código de tal manera que no se tengan problemas en la clonación de recursos.
#   - Es importante utilizar sincronizadores (se verán más adelante) para que no exista pérdida de información.
