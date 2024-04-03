# Importar librerías
import threading
import requests
from bs4 import BeautifulSoup
import json

# URL Base
url_base = "https://quotes.toscrape.com/page/{}"
dict_contenido = {}


# Definir función
def extraer_links_url(url: str, clave: str) -> None:
    
    """
    Extrae citas del sitio web
    """
    
    # Extraer
    r = requests.get(url)
    # Revisar estado
    if r.status_code == 200:
        # Convertir extracción a código HTML
        soup = BeautifulSoup(r.content, "html.parser")
        # Encontrar divs con clase "quote"
        divs = soup.findAll(name="div", attrs={"class": "quote"})
        dict_contenido[clave] = []
        for cita in divs:
            texto = cita.find("span").get_text()
            dict_contenido[clave].append(texto)
    else:
        dict_contenido[clave] = "N/A"
        
    
# Crear e inicializar los Hilos
lista_hilos = []
for i in range(1, 11):
    t = threading.Thread(target=extraer_links_url, kwargs={"url": url_base.format(i), "clave": f"Pag_{i}"})
    # Agregar cada objeto se crea a la lista
    lista_hilos.append(t)
    t.start()
    
# Esperar a cada Hilo
for t in lista_hilos:
    t.join()
    

# Mostrar citas/frases
print(json.dumps(dict_contenido, indent=4)) # Dar formato
print("Programa ha finalizado")

# Recordatorio:
#   - Join nos permite esperar a que un Hilo termine su ejecución antes de continuar con el resto
#     de la ejecución del código.
