'''
Transmisor de Audio utilizando SPI (Para un TLV5616)
@author: David Josue Barrientos Rojas (2014)
d[dot]b[dot]gt[at]ieee[dot]org
Universidad de San Carlos de Guatemala
EE School
'''

import spidev
import time
import socket
import wave
import numpy
import scipy.io.wavfile
import thread
import os

IP = '192.168.1.59'
Puerto=7777
paquetes=20
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, Puerto))
server.listen(1)
print '----------------------------'
print 'Conecte el Cliente por favor'
print '----------------------------'
conn, addr = server.accept() 
print 'Conectado con: ', addr
print '\nCrtl-C para terminar la conexion'

def Reproductor(Audio,Inicio):
    os.system("sudo aplay sound.wav &")
    thread.exit()



spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 2048000
muestras=[]


try:
    while True:
        a=conn.recv(paquetes)
        a=raw_input('Segundos a grabar: ')
        print "Muestreando durante " + a +" segundo(s)"
        a=(int(a)*44100)
        b=conn.recv(paquetes)
        b=raw_input('Frecuencia de Corte del Filtro: ')

        for i in range(0,a):
            smp = spi.xfer2([0x00])
            muestras.append(smp[0])

        for i in range(len(muestras)):
            muestras[i]=(muestras[i]-127.5)*256

        ms=numpy.array(muestras)
        print ms
        ms=numpy.int16(ms)
        scipy.io.wavfile.write('Prueba.wav',44100, ms)
    thread.start_new_thread(Reproductor, ('Prueba.wav',0))


                
except KeyboardInterrupt:
    print ('Terminando Programa')
    conn.close()

