import requests
from bs4 import BeautifulSoup
import pandas as pd
import pytesseract as tess

class do_scraping():
    def __init__(self):
        self.ok= "ok"
    def step1_request():
        url = "http://ikospain.blogspot.com/search/label/Comité%20Directivo"

        res = requests.get(url)

        soup = BeautifulSoup(res.content, "html.parser")

        elements =  soup.find_all("div", attrs={"class":"separator"})

        # def look_inside(web_elements):
        #     for i in web_elements:
        #         print(f"\n [{web_elements.index(i)}]",i)

        # look_inside(elements)

        img_url = elements[0].find("a").get("href")
        return img_url

    def step2_download(img_url):
        filename = "comite_deportivo_kyokushin"
        directorio = "D:/PYTHON FILES/Web Scraping/img"

        imagen = requests.get(img_url)
        with open(f"{directorio}/{filename}.jpg", "wb") as f:
            f.write(imagen.content)

#---- Me salto la parte de tesseract ya que no se obtuvo el resultado deseado ----
    # # https://pythondiario.com/2018/08/extraer-texto-de-imagenes-con-ocr.html
    # tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # imagen= r"D:/PYTHON FILES/Web Scraping/img/comite_deportivo_kyokushin.jpg"
    # texto = tess.image_to_string(image= imagen, lang="eng+spa")
    # languaje = tess.get_languages(imagen)
#---- ----
    def step3_dataframe():
        datos_obtenidos = {
            "posición":["SHIHAN","SHIHAN","SENSEI","SENSEI","SENSEI","SEMPAI","SEMPAI","SEMPAI","SENSEI","SENSEI","SENSEI","SENSEI","SEMPAI"],
            "nombre":["DANIEL LORENTE","TONI ROCA","LORENZO MARTINEZ","ANDRES GALLEGO","SALVA CRESPO","VICTOR CABRERA","HECTOR CERDEÑA","ADRIA ALIMANY","ANGEL ROMERO","OLIVER AGUILERA","XAVI FOSCH","INMA MARQUEZ","JOSE M. PERAL"],
            "sexo":["M","M","M","M","M","M","M","M","M","M","M","F","M"],
            "cargo":["Presidente & Branch Chief","Vice-presidente","Secretario","Relaciones Internacionales","Preparador físico selección","Vocal","Vocal","Vocal","Vice-presidente","Tesorero","Desplazamientos","Logística selección","Summer camp"],
        }

        df = pd.DataFrame(datos_obtenidos)

        jerarquias = {'SHIHAN': 3, 'SENSEI': 2, 'SEMPAI': 1}
        df['jerarquia'] = df['posición'].map(jerarquias)
        df = df.sort_values('jerarquia', ascending=False).reset_index(drop=True)
        df = df.drop('jerarquia', axis=1)
        df.loc[13] = df.iloc[9] # hago copia del 9
        df.iloc[9] = df.iloc[12] # muevo el 12 al 9
        df.iloc[12] = df.iloc[13] # muevo la copia de 9 al 12
        df.loc[2:] = df.loc[2:].shift(1) # aprovecho que me sobra 13 para pisarlo con un arrastre
        df.iloc[2] = df.iloc[6] # muevo el 6 al 2, que contiene NaN del arrastre
        df = df.drop(6,axis=0) # elimino 6
        return df