# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
punto py 
"""
#foto1=Image.open("C:\\Users\\annie\\Documents\\Lab_imagenes_4.jpg")
#Mostrar la imagen 
#foto1.show()
#foto_cop = cv2.resize(foto3,(780,780))
from PIL import Image
import numpy as np 
import cv2
from cv2 import resize


# Se tiene que guardar las imagenes 
    foto3 = cv2.imread("Lab_imagenes_4.jpg")
# Se hace la piramide gausiana y seguido la piramide laplaciana     
    pyrone = cv2.pyrDown(foto3)
    laplaone = cv2.substract(foto3 ,cv2.pyrUp(pyrone))
    
    pyrtwo = cv2.pyrDown(pyrone)
    laplatwo = cv2.substract(pyrone ,cv2.pyrUp(pyrone))
     
    pyrthree = cv2.pyrDown(pyrtwo)
    laplathree = cv2.substract(pyrthree)
    
    pyrfour = cv2.pyrDown(pyrthree)
    laplafour = cv2.substract(pyrfour)
    
    pyrfive = cv2.pyrDown(pyrfour)
    laplafive = cv2.substract(pyrfive)
   
    
    pyrsix  = cv2.pyrDown(pyrfive)
   laplasix = cv2.substract(pyrsix)
   
#Para mostrar las imagenes
#cv2.imshow('blahblah',imagen)
#comando=cv2.waitKey(0)   
#if conmando
#cv2.destroyAllWindows()