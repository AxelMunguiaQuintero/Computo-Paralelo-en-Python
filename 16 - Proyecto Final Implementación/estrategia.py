# Importar librerí­as
import pandas as pd
import numpy as np
import requests
from datetime import datetime


# Definir función
class Crypto_Estrategia:
    
    """
    Clase que analiza una gran cantidad de activos en paralelo y determina en que instrumentos
    financieros se deberí­a de invertir dinero.
    """
    
    # Constructor
    def __init__(self) -> None:
        
        """
        Constructor.
        """
        
        # Definir atributos
        self.instrumentos_financieros = None
        self.url_base = "https://api.binance.com"
        self.endpoint_instrumentos = "/api/v3/exchangeInfo"
        self.endpoint_datos = "/api/v3/klines"
        # Documentación
        self.documentacion = "https://binance-docs.github.io/apidocs/"
        
    
    def obtener_activos(self) -> None:
        
        """
        Guarda en la variable instrumentos_financieros todos los activos sobre los cuales se puede pedir información histórica.
        """
        
        # Obtener
        r = requests.get(self.url_base + self.endpoint_instrumentos, params=dict())
        if r.status_code == 200:
            informacion = r.json()
            activos = [x["symbol"] for x in informacion["symbols"]]
            self.instrumentos_financieros = activos

    
    def obtener_datos(self, instrumento: str, intervalo: str = "1m", limite: int = 1_000) -> pd.DataFrame:
        
        """
        Obtiene datos historicos de un instrumento financiero.
        
        ----------
        Parámetros:
        ----------
        param : str : instrumento : Símbolo del activo.
        ----------
        param : str : intervalo : Ventana de tiempo (por defecto, se establece en '1m').
        ----------
        param : int : limite :  Limite de datos que traerá (por defecto, se establece en 1500).
        ----------
        Salida:
        ----------
        return : pd.DataFrame : Cálculo del Cruce de Medias Móviles.
        """
        
        # Crear diccionario con parámetros para Binance
        params = dict()
        params["symbol"] = instrumento
        params["interval"] = intervalo
        params["limit"] = limite
        # Realizar petición web
        r = requests.get(self.url_base + self.endpoint_datos, params=params)
        if r.status_code == 200:
            datos = r.json()
            candles = []
            for c in datos:
                # (Time, Open, High, Low, Close, Volume)
                hora = datetime.utcfromtimestamp(int(float(c[0]) / 1_000)).strftime('%Y-%m-%d %H:%M:%S')
                candles.append((hora, float(c[1]), float(c[2]), float(c[3]), float(c[4]), float(c[5])))
            df = pd.DataFrame(candles, columns=["Time", "Open", "High", "Low", "Close", "Volume"])
            df.set_index("Time", inplace=True)
            
            return df
        
        
    def Cruce_MA(self, df: pd.DataFrame, longitud_rapida: int = 9, longitud_lenta: int = 26) -> pd.DataFrame:
        
        """
        El Cruce de Medias Móviles es un indicador técnico que utiliza dos MAs como estrategia. Es un buen ejemplo de las llamadas
        estrategias tradicionales. Las estrategias tradicionales son siempre largas o cortas, lo que significa que nunca están fuera del mercado.
        
        Cómo operar con ello:
            
            Operar con Cruce de MA es bastante simple. Si la MA rápida cruza desde abajo hacia arriba de la MA lenta, esto significa
            una oportunidad de compra. Si la MA rápida cruza desde arriba hacia abajo de la MA lenta, esto significa una oportunidad de venta.
            El Cruce de MA se utiliza a menudo en conjunto con otros indicadores para evitar señales falsas en mercados de baja volatilidad.
            
        Para ver un ejemplo, por favor visita la siguiente URL:
            
            https://bit.ly/3r7NiTK
            
        ----------
        Parámetros:
        ----------
        param : pd.DataFrame : df : Datos.
        ----------
        param : int : longitud_rapida : Ventana rápida a utilizar en el cálculo del Cruce de MA (por defecto, se establece en 9).
        ----------
        param : int : longitud_lenta : Ventana lenta a utilizar en el cálculo del Cruce de MA (por defecto, se establece en 26).
        ----------
        Salida:
        ----------
        return : pd.DataFrame : Cálculo del Cruce de Medias Móviles.
        """
        
        # Calcular
        columna_precio = df["Close"]
        MA_Rapida = columna_precio.rolling(window=longitud_rapida).mean()
        MA_Rapida_S = MA_Rapida.shift(periods=1)
        MA_Lenta = columna_precio.rolling(window=longitud_lenta).mean()
        MA_Lenta_S = MA_Lenta.shift(periods=1)
        # Cruzar
        Cruce = np.where(((MA_Rapida > MA_Lenta) & (MA_Lenta_S > MA_Rapida_S)), 1,
                         np.where(((MA_Rapida < MA_Lenta) & (MA_Lenta_S < MA_Rapida_S)), -1, 0))
        Cruce_MA = pd.concat([MA_Rapida, MA_Lenta, pd.Series(Cruce, index=df.index)], axis=1)
        
        Cruce_MA.columns = ["MA_Rapida", "MA_Lenta", "Cruce"]
        
        return Cruce_MA


# Ejecutar
if __name__ == "__main__":
    # Realizar demostración
    ce = Crypto_Estrategia()
    # Obtener todos los instrumentos financieros posibles
    print("El número de activos inicial es: ", ce.instrumentos_financieros)
    ce.obtener_activos()
    print("El número de activo para pedir información es: ", len(ce.instrumentos_financieros))
    # Obtener datos de un instrumento
    instrumento = "BTCUSDT" # Bitcoin
    datos = ce.obtener_datos(instrumento)
    print(datos)
    # Calcular estrategia
    calculo_estrategia = ce.Cruce_MA(datos)
    senales = calculo_estrategia
    print(senales)
