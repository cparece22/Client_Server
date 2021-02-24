import RoboPiLib as RPL
import setup
from time import sleep
###EDIT THESE IF NEEDED
'''
L = 0
R = 1
'''
A = 0
motors = [0] ###If extra motors add pin # here

def extend():
  RPL.servoWrite(A,2000)
def retract():
  RPL.servoWrite(A,1000)
def stop():
  for x in motors:
    RPL.servoWrite(x,0)

'''
def front():
  RPL.servoWrite(L,1600)
  RPL.servoWrite(R,1400)

def left():
  RPL.servoWrite(L,1500)
  RPL.servoWrite(R,1400)

def right():
  RPL.servoWrite(L,1600)
  RPL.servoWrite(R,1500)

def back():
  RPL.servoWrite(L,1400)
  RPL.servoWrite(R,1600)
'''
