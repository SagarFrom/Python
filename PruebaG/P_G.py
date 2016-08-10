from distutils import command
from tkFileDialog import askopenfile

import cv2
import numpy as np
from matplotlib import pyplot as plt
from Tkinter import *
import subprocess



from PIL import Image,ImageTk

import tkFileDialog


form1=Tk()
backruta = "C:\Users\Administrator\PycharmProjects\PruebaG\upcbackgroundphython.png"
ayudaruta = "C:\Users\Administrator\PycharmProjects\PruebaG\Guia-Uso-Trabajo-Histograma.docx"

#imgBackground = PhotoImage(backruta)
#imgBackground.width = 100
#imgBackground.height = 100
#lab = Label(form1, image=imgBackground)
#lab.grid(row=1,column=1)
#lab.pack()



form1.title("ECUALIZACION MATEMATICA COMPUTACIONAL");

form1.iconbitmap('mc.ico')
form1.geometry("500x500")
l1=Label(form1,text="BIENVENIDO AL PROYECTO")
l1.pack()
l2=Label(form1,text="ECUALIZACION GLOBAL DE HISTOGRAMA")
l2.pack()

l3=Label(form1,text="")
l3.pack()

l4=Label(form1,text="PROFESOR: CRIBILLERO ACHING, JUAN AURELIO")
l4.pack()

l5=Label(form1,text="CURSO: MATEMATICA COMPUTACIONAL")
l5.pack()
l6=Label(form1,text="SECCION: SI44")
l6.pack()

l7=Label(form1,text="")
l7.pack()
l8=Label(form1,text="INTEGRANTES:")
l8.pack()
l9=Label(form1,text="TICONA JUAN")
l9.pack()
l10=Label(form1,text="SANCHEZ MIGUEL")
l10.pack()
l11=Label(form1,text="CORDOVA MIGUEL")
l11.pack()

def mostrarAyuda():
    path_to_file = ayudaruta
    path_to_program = r'C:\Program Files (x86)\Microsoft Office\Office15\WINWORD.EXE'
    subprocess.Popen("%s %s" % (path_to_program, path_to_file))

def task():
    global imgBase
    imgBase = 0

def InsertarImagen():
    global imgBase

    filename = askopenfile(mode='r')

    if filename is None :
        return

    filename.close()


    rutafile=filename.name
    print rutafile
    imgBase = cv2.imread(rutafile,0)
    cv2.imshow("ORIGINAL",imgBase)

def showimage():
    global imgBase
    if imgBase is 0:
        return

    print imgBase


    cv2.imshow('ORIGINAL',imgBase)

def showimageMod():
    global imgBase
    if imgBase is 0:
        return

    print imgBase

    equ = cv2.equalizeHist(imgBase)
    imgTransformacion = np.hstack((imgBase,equ))
    cv2.imshow('ORIGINAL - MODIFICADA',imgTransformacion)

def showHistOriginal():
    global imgBase
    if imgBase is 0:
        return

    print imgBase

    plt.clf()
    #imgOriginal = cv2.imread('wiki.jpg',0)
    hist,bins = np.histogram(imgBase.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf *hist.max()/ cdf.max()
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(imgBase.flatten(),255,[0,255], color = 'r')
    plt.xlim([0,255])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.title('Histograma F. Original')
    plt.show()

def showHistModificada():
    global imgBase
    if imgBase is 0:
        return

    print imgBase

    plt.clf()
    #imgBase = cv2.imread('wiki.jpg',0)
    equ = cv2.equalizeHist(imgBase)
    imgTransformacion = np.hstack((imgBase,equ))
    hist,bins = np.histogram(equ.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf *hist.max()/ cdf.max() # this line not necessary.
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(equ.flatten(),255,[0,255], color = 'r')
    plt.xlim([0,255])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.title('Histograma F. Modificada')
    plt.show()


menu1 = Menu(form1)
form1.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="IMAGENES", menu=menu1_1)
menu1_1_1 = Menu(menu1_1, tearoff=0)

menu1_1.add_command(label="IMAGEN ORIGINAL",command=lambda: showimage())
menu1_1.add_separator()

menu1_1.add_command(label="IMAGEN MODIFICADA",command=lambda: showimageMod())


menu2 = Menu(form1)
form1.config(menu=menu1)
menu2_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="HISTOGRAMAS", menu=menu2_1)
menu2_1_1 = Menu(menu2_1, tearoff=0)

menu2_1.add_command(label="HISTOGRAMA ORIGINAL",command=lambda: showHistOriginal())
menu2_1.add_separator()

menu2_1.add_command(label="HISTOGRAMA MODIFICADA",command=lambda: showHistModificada())

menu3_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="ARCHIVO", menu=menu3_1)
menu3_1.add_command(label="SUBIR IMAGEN",command=lambda: InsertarImagen())

menu4_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="AYUDA", menu=menu4_1)
menu4_1.add_command(label="MOSTRAR MANUAL",command=lambda: mostrarAyuda())



form1.after(10, task)
form1.mainloop()



#hist,bins = np.histogram(img.flatten(),256,[0,256])
#
#cdf = hist.cumsum()
#cdf_normalized = cdf *hist.max()/ cdf.max() # this line not necessary.
#
#cdf_m = np.ma.masked_equal(cdf,0)
#cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
#cdf = np.ma.filled(cdf_m,0).astype('uint8')
#
#img2 = cdf[img]
#
#img = cv2.imread('wiki.jpg',0)
#equ = cv2.equalizeHist(img)
#res = np.hstack((img,equ)) #stacking images side-by-side
#cv2.imwrite('res.png',res)
#
#img = cv2.imread('res.png',0)
#
#cv2.imshow('wiki.jpg',img)
#cv2.imshow('wiki2.jpg',img2)
#
##cv2.imshow('res.png',res)
#
##cv2.waitKey(0)
#
#plt.plot(cdf_normalized, color = 'b')
#plt.hist(img.flatten(),255,[0,255], color = 'r')
#plt.xlim([0,255])
#plt.legend(('cdf','histogram'), loc = 'upper left')
#plt.title('Histograma F. Original')
#plt.show()
#
#plt.plot(cdf_normalized, color = 'b')
#plt.hist(img2.flatten(),255,[0,255], color = 'r')
#plt.xlim([0,255])
#plt.legend(('cdf','histogram'), loc = 'upper left')
#plt.title('Histograma F. Original')
#plt.show()


