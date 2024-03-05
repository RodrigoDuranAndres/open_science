# open_science

Este codigo relaliza un analisis de los pdfs en la carpeta paepers gracias a grobid.
El resultado de dicho analisis se pasa ha output, da un xml cunado funiona correctamente y un txt cuando no.

De cada xml, se hace un wordcloud de la introducción y un listado delas urls escritas en el.
Tambien se hace un histograma con la cantidad de figuras en cada paper.

# Enlances de los papers

|                         paper name                        |                        url                     |
|-----------------------------------------------------------|------------------------------------------------|
|Adversarial-Diffusion-Distillation                         |  [Link](https://arxiv.org/pdf/2311.17042.pdf)  |
|CLIP-Connecting-text-and-images                            |  [Link](https://arxiv.org/pdf/2103.00020.pdf)  |
|Consistency-Models                                         |  [Link](https://arxiv.org/pdf/2303.01469.pdf)  |
|DALL·E-Creating-images-from-text                           |  [Link](https://arxiv.org/pdf/2102.12092.pdf)  |
|GEMINI-Measuring-Massive-Multitask-Language-Understanding  |  [Link](https://arxiv.org/pdf/2009.03300.pdf)  |
|LATENT-CONSISTENCY-MODELS                                  |  [Link](https://arxiv.org/pdf/2310.04378.pdf)  |
|LCM-LoRA                                                   |  [Link](https://arxiv.org/pdf/2311.05556.pdf)  |
|Llama2-Open-Foundation-and-Fine-Tuned-Chat-Models          |  [Link](https://arxiv.org/pdf/2307.09288.pdf)  |
|mistral                                                    |  [Link](https://arxiv.org/pdf/2401.04088.pdf)  |
|NIPS-2017-attention-is-all-you-need-Paper                  |  [Link](https://arxiv.org/pdf/1706.03762.pdf)  |

## Para Ejecutarse

Tines que tener python 3.11 (o más) y  un container de la imagen de grobid/grobid
intruciones: https://grobid.readthedocs.io/en/latest/Grobid-docker/
Exponerlo en el puerto predeterminado (8070)

Luego ejecutarlo con el comando:
```bash
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0
```

Para instalar la libreria grobid sigua las instuciones (ya hemos clonado el github de [git clone https://github.com/kermitt2/grobid_client_python], por tanto, estando en la misma carpeta del github):
```bash
py .\grobid_client_python\setup.py install
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
