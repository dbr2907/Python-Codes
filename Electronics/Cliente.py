
import time, os, serial, socket



TCP_IP= '192.168.1.55'
TCP_PORT=7777
BUFFER_SIZE=20
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((TCP_IP, TCP_PORT))

try:
	while True:
		comando = raw_input()
		server.send(comando)
		print comando

except KeyboardInterrupt:
	print 'Terminando Programa'

		

