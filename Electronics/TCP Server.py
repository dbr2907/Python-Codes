#TCP Server
#David Josue Barrientos Rojas (2017)
#d[dot]b[dot]gt[at]ieee[dot]org
#Universidad de San Carlos de Guatemala
#EE School




import socket

import serial

import time



#-------------------------------------------------------
                 
#Inicializacion

#-------------------------------------------------------

IP = '192.168.1.80'

Puerto=7777

paquetes=20

uart=serial.Serial('/dev/ttyUSB0', 9600, timeout=5)

uart.flushInput()

uart.flushOutput()

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((IP, Puerto)) 


#-------------------------------------------------------

server.listen(1)

print '----------------------------'

print 'Conecte el Cliente por favor'

print '----------------------------'

conn, addr = server.accept() 

print 'Conectado con: ', addr

print '\nCrtl-C para terminar la conexion'

#-------------------------------------------------------

#                    Main

#-------------------------------------------------------


try:
    
	while True:
        
		comando=conn.recv(paquetes)  
	
 		uart.write(comando)		
			
except KeyboardInterrupt:
    
	uart.close()
    
	conn.close()
