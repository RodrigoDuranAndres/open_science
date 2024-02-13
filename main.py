import os
import xml.etree.ElementTree as ET
from grobid_client.grobid_client import GrobidClient
from utils import utils

# Directorio donde se encuentran los archivos XML
directorio = './output/papers'
numero_figuras_paper = []
listado_archivos = []

client = GrobidClient(config_path="./config.json")
client.process("processFulltextDocument", ".", output="./output/", consolidate_citations=True, tei_coordinates=True, n=20)

# Bucle para recorrer todos los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith('.xml'):  # Verificar si el archivo es un XML
        listado_archivos.append(archivo[:5])
        ruta_completa = os.path.join(directorio, archivo)
        
        tree = ET.parse(ruta_completa)
        root = tree.getroot()

        imagen = utils.wordcloud_pdf(root)
        imagen.savefig("./output/imagenes/" + archivo[:-13] + ".png", bbox_inches='tight')

        numero_figuras_paper.append(utils.contador_figuras(root))

        print(list(utils.buscar_enlaces(root)))

if listado_archivos:
    utils.histograma_figuras(listado_archivos, numero_figuras_paper)
