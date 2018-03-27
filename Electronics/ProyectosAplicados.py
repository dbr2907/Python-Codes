import socket
import serial
import time
import thread
#-----------------------------------
#              PID
#-----------------------------------
global puntop

class PID(object):
    """
    Sistema de control PID discreto
    """

    def __init__(self, P=2.0, I=1.0, D=0.0, Derivator=0, Integrator=0, Integrator_max=255, Integrator_min=75):
        """
        Inicializa el sistema de control, estableciendo
        las condiciones iniciales
        """
        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.Derivator=Derivator
        self.Integrator=Integrator
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min

        self.set_point=0.0
        self.error=0.0

    def update(self,current_value):
        """
    Calcula la salida del PID para un valor de referencia de entrada
    (set point) y la retroalimentacion
    """

        self.error = self.set_point - current_value        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * ( self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value
        self.PID_value = PID
        return PID

    def setPoint(self,set_point):
        """
        Inicializar el set point del PID.
        """
        self.set_point = set_point
        self.Integrator=0
        self.Derivator=0

    def setIntegrator(self, Integrator):
        self.Integrator = Integrator

    def setDerivator(self, Derivator):
        self.Derivator = Derivator

    def setMaxIntegrator(self, maxIntegrator):
        self.Integrator_max = maxIntegrator

    def setMinIntegrator(self, minIntegrator):
        self.Integrator_min = minIntegrator

    def setKp(self,P):
        self.Kp=P

    def setKi(self,I):
        self.Ki=I

    def setKd(self,D):
        self.Kd=D

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator


#-------------------------------------------------------
#                Hilo
#-------------------------------------------------------
def Hilo(x,y):
    global puntop
    IP = '192.168.1.157'
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

#---------------------------------------
#                LOOP
#---------------------------------------

    try:
        while True:
            comando=conn.recv(paquetes) 
            if (comando=='5'):
                puntop=250
            elif (comando=='4'):
                puntop=225
            elif (comando=='3'):
                puntop=200
            elif (comando=='2'):
                puntop=175
            elif (comando=='1'):
                puntop=150
            elif (comando=='0'):
                puntop=0
            crv.setPoint(puntop)
            if(comando=='t'):
                uart.write(comando)
                time.sleep(0.1)
                a=uart.readline()
                conn.send(a)
                print a
            elif(comando=='q'):
                thread.exit()
            else:
                uart.write(comando)
            uart.flushOutput()
#-----------------------------------------------------
#               Crtl+c
#-----------------------------------------------------

    except KeyboardInterrupt:
        uart.close()
        conn.close()
#----------------------------------------------
#           Inicio Hilo y Main
#-----------------------------------------------

def Main(w,z):
    while True:
       
        uart.write('e')
        b=uart.readline()
        b=int(b)
        Np=crv.update(b)
        if(Np>75 and Np<=150):
            uart.write('1')
        elif(Np>150 and Np<=175):
            uart.write('2')
        elif(Np>175 and Np<=200):
            uart.write('3')
        elif(Np>200 and Np<=225):
            uart.write('4')
        elif(Np>225 and Np<=250):
            uart.write('5')
        
        
#-------------------------------------------------------
#                  Inicializacion
#-------------------------------------------------------

uart=serial.Serial('/dev/ttyACM0', 9600, timeout=5)
uart.flushInput()
uart.flushOutput()
puntop=0
crv=PID()
Kp = 0.8
Ki = 0.2
Kd = 0
crv.setKp(Kp)
crv.setKi(Ki)
crv.setKd(Kd)
thread.start_new_thread(Hilo(0,0))
Main(0,0)
    
    
