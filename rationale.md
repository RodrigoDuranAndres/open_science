## Resumen

Este codigo relaliza un analisis de los pdfs en la carpeta paepers gracias a grobid.
El resultado de dicho analisis se pasa ha output, da un xml cunado funiona correctamente y un txt cuando no.

De cada xml, se hace un wordcloud de la introducción y un listado delas urls escritas en el.
Tambien se hace un histograma con la cantidad de figuras en cada paper.

## Para Ejecutarse

Tines que tener un container de la imagen de grobid/grobid
intruciones: https://grobid.readthedocs.io/en/latest/Grobid-docker/
Exponerlo en el puerto predeterminado (8070)

Luego ejecutarlo con el comando:
```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0
```

Para instalar la libreria grobid sigua las instuciones:
```bash
git clone https://github.com/kermitt2/grobid_client_python
cd grobid_client_python
python3 setup.py install
```
Source: https://github.com/kermitt2/grobid_client_python/tree/master


Para el resto de librerias instalar requiremets:
```bash
pip install -r requirements.txt
```

Elminar los ficheros contenidos en la carpeta ouput, para que se sobreescriban con tu resultado.

Posteriormente ejecutar main:
py main.py

Tambien tienes la opción de hacerlo mismo que el main.py con el cuaderno analisis_papers.ipynb, si lo prefiere.



