# IBIO4490
This repository strictly follows the teorethical guidelines provided by the course "*IBIO4490 - Computer Vision*" at Uniandes. 
**2019**
import   wget
# Dirección de la cual seva a descargar   la información
url=‘http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz’
# Descargar la información de la pagina 
data=wget.download(url)
control d 
# Se hizo untar con Linux 
 tar -xzvf BSR_bsds500.tgz
Import os 
# Creo unacarpeto nuevo la cual se va a encontrar en amvelosa/BSR/BSDS500/data
os.mkdir(“IMG”)
os.listdir(".")
# se entra a images/test
Cd images/test
# se adquieren los nombres de las carpetas
Python 
import os 
ana=os.listdir(".")
# se quiere crear 6 random números
import random 
from random import shuffle 
list= [i for i in range(200)]
shuffle(list)
num=list[:6]
primero=ana[num[1]]
segundo= ana[num[2]]
tercero =ana[num[3]]
cuarto = ana[num[4]]
quinto= ana[num[5]]
sexto =ana[num[0]]
import os 
import shutil 
# Copio los randoms y los pego en la carpeta Nuevo 
shutil.copy(primero,"../../Nov.jpg")
shutil.copy(segundo,"../../Nov2.jpg")
shutil.copy(tercero,"../../Nov3.jpg")
shutil.copy(cuarto,"../../Nov4.jpg")
shutil.copy(quinto,"../../Nov5.jpg")
shutil.copy(sexto,"../../Nov6.jpg")
# Salimos de python y movemos las imágenes a la carpeta Img
cd .. 
cd .. 
cp -i Nov.jpg IMG/
cp -i Nov2.jpg IMG/
cp -i Nov3.jpg IMG/
cp -i Nov4.jpg IMG/
cp -i Nov5.jpg IMG/
cp -i Nov6.jpg IMG/
# entramos a la carpeta de Img 
Cd IMG/ 
# le hacemos reshpae a las imágenes
Python 
# Se hace abren las imágenes y se hace reshape

from PIL import Image
import requests
from io import BytesIO

nov = Image.open("Nov.jpg")
resep=nov.resize((256,256))
nov2 = Image.open("Nov2.jpg")
resep2=nov2.resize((256,256))
