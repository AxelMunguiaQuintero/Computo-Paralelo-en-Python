# Importar librerías
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


# URL Base
urls = ["https://quotes.toscrape.com/page/{}".format(i) for i in range(1, 11)]


# Definir función
def extraer_links_url(url: str) -> None:
    
    """
    Extrae citas del sitio web
    """
    
    # Extraer
    r = requests.get(url)
    citas = []
    # Revisar estado
    if r.status_code == 200:
        # Convertir extracción a código HTML
        soup = BeautifulSoup(r.content, "html.parser")
        # Encontrar divs con clase "quote"
        divs = soup.findAll(name="div", attrs={"class": "quote"})
        for cita in divs:
            texto = cita.find("span").get_text()
            citas.append(texto)
    else:
        citas.append("N/A")
        
    return citas


# Inicializar
tpx = ThreadPoolExecutor(max_workers=4)
# Enviar tarea por tarea
citas = [tpx.submit(extraer_links_url, url) for url in urls]
# Imprimir para ver el estado de cada Hilo/Trabajador
print(citas)

# Revisar si el resultado está listo
for i in range(len(citas)):
    # .result() es similar .join()
    if citas[i].result(): # Mientras el resultado no esté listo, esperará como si fuese un .join()
        # Reasignar el valor
        citas[i] = citas[i].result()
# Volvemos a imprimir para ver la extracción
print(citas[0])

# Utilizando Map
citas_map = tpx.map(extraer_links_url, urls)
# Extraer resultados (similar a .join en Hilos)
citas_map = [i for i in citas_map]
# Cerrar nuestro ejecutor
tpx.shutdown(wait=True)
# Mostrar primera extracción
print(citas_map[0])

# Recordatorio:
#   - Los grupos de ejecución son una herramienta que se encargará de realizar una lista de tareas.
#   - Son convenientes, pues evitan la creación y destrucción de Hilos y esto mejora la eficiencia de nuestra aplicación.
