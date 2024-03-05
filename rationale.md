## Resumen

Este codigo relaliza un analisis de los pdfs en la carpeta papers gracias a grobid.
El resultado de dicho analisis se pasa ha output, da un xml cunado funiona correctamente y un txt cuando no.

De cada xml, se hace un wordcloud de la introducción y un listado delas urls escritas en el.
Tambien se hace un histograma con la cantidad de figuras en cada paper.
Cada una de estas tareas estan definidas en su propia función en utils/utils.py

Las intruciones en el README.md son para ejecutar el python, pero si prefiere hacerlo en cuaderno puede usar analisis_papers.ipynb, despues de ejecutar el .\grobid_client_python\setup.py





