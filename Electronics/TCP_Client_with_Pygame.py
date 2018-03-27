'''
TCP Client in Python using an external 
controller with pygame to control a robot
@author: David Josue Barrientos Rojas (2015)
d[dot]b[dot]gt[at]ieee[dot]org
Universidad de San Carlos de Guatemala
EE School
'''

import pygame, time, os, serial, socket



def JoystickConf():
    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    joy = pygame.joystick
    idx = 0
    gamePad = joy.Joystick(idx)
    gamePad.init()
    return gamePad

def JoyButtons(gamePad):
    pygame.event.pump()
    out =[]
    for i in range(gamePad.get_numaxes()):
        out.append(int(gamePad.get_axis(i)*10)/10.0)
    for i in range(gamePad.get_numbuttons()):
        out.append(gamePad.get_button(i))
    os.system('clear')
    
    if (out[6]==1):
        direc="v"
    elif (out[7]==1):
        direc="b"
    elif (out[8]==1):
        direc="n"
    elif (out[9]==1):
        direc="m"
    elif (out[2]>0):
        direc="g"
    elif (out[3]>0):
        direc="f"
    elif (out[0]>0 and out[1]>0):
        direc="c"
    elif (out[0]<0 and out[1]>0):
        direc="z"
    elif (out[0]>0 and out[1]<0):
        direc="e"
    elif (out[0]<0 and out[1]<0):
        direc="q"
    elif (out[0]==0 and out[1]>0):
        direc="x"
    elif (out[0]==0 and out[1]<0):
        direc="w"
    elif (out[0]<0 and out[1]==0):
        direc="a"
    elif (out[0]>0 and out[1]==0):
        direc="d"
    else:
        direc="s"
    return direc    
TCP_IP= '10.50.43.135'
TCP_PORT=7777
BUFFER_SIZE=20
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((TCP_IP, TCP_PORT))
joystickRate = 0.2
gPad = JoystickConf()

try:
    while True:
        comando = JoyButtons(gPad)
        server.send(comando)
        print comando
        time.sleep(joystickRate)
except KeyboardInterrupt:
    print 'Terminando Programa'

        

