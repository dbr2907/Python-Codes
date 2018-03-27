'''
Codigo para encontrar el footprint de tres canciones
@author: David Josue Barrientos Rojas (2013)
d[dot]b[dot]gt[at]ieee[dot]org
Universidad de San Carlos de Guatemala
EE School
'''


import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import sys

temp=[]
peaks=[]


mues,datos = wav.read('Peces.wav')
tpaso = int(mues * 0.01161) #512
tven  = int(mues * 0.02322)  #1024
nfft = tven #1024
ventana = np.hamming(tven)
nn = range(tven, len(datos), tpaso)
X = np.zeros( (len(nn), nfft/2) )

for i,n in enumerate(nn):
    xseg = datos[n-tven:n]
    z = np.fft.fft(ventana * xseg, nfft)
    Y=np.abs(z[:nfft/2])
    X[i,:] = Y

ftp=[]
maximos=[]
for k in range(len(X)-1):
    tmp=int(max(X[k]+X[k+1]))
    maximos.append(tmp)
h=max(maximos)
l=min(maximos)

for n in range(len(maximos)):
    maximos[n]=(255*maximos[n])/(h-l)

mues,datos = wav.read('Chispa.wav')
tpaso = int(mues * 0.01161) #512
tven  = int(mues * 0.02322)  #1024
nfft = tven #1024
ventana = np.hamming(tven)
nn = range(tven, len(datos), tpaso)
X = np.zeros( (len(nn), nfft/2) )

for i,n in enumerate(nn):
    xseg = datos[n-tven:n]
    z = np.fft.fft(ventana * xseg, nfft)
    Y=np.abs(z[:nfft/2])
    X[i,:] = Y

ftp2=[]
maximos2=[]
for k in range(len(X)-1):
    tmp=int(max(X[k]+X[k+1]))
    maximos2.append(tmp)
h=max(maximos2)
l=min(maximos2)

for n in range(len(maximos2)):
    maximos2[n]=(255*maximos2[n])/(h-l)

mues,datos = wav.read('Star.wav')
tpaso = int(mues * 0.01161) #512
tven  = int(mues * 0.02322)  #1024
nfft = tven #1024
ventana = np.hamming(tven)
nn = range(tven, len(datos), tpaso)
X = np.zeros( (len(nn), nfft/2) )

for i,n in enumerate(nn):
    xseg = datos[n-tven:n]
    z = np.fft.fft(ventana * xseg, nfft)
    Y=np.abs(z[:nfft/2])
    X[i,:] = Y

ftp3=[]
maximos3=[]
for k in range(len(X)-1):
    tmp=int(max(X[k]+X[k+1]))
    maximos3.append(tmp)
h=max(maximos3)
l=min(maximos3)

for n in range(len(maximos3)):
    maximos3[n]=(255*maximos3[n])/(h-l)

for i in range(len(maximos)-432):
    for j in range(430):
        ftp[i]+=maximos[i+j]

print ftp   