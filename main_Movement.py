import RoboPiLib as RPL
import setup
import motor_Direction
from time import sleep

def movement(data):
    usrin = data
    if usrin == '1':
        motor_Direction.extend()
    elif usrin == '2':
        motor_Direction.retract()
    elif usrin == '0':
        motor_Direction.stop
    else:
        print("failed, input not recognized")

    '''
      if usrin == 'w':
        direction.front()
      elif usrin == 's':
        direction.back()
      elif usrin == 'a':
        direction.left()
      elif usrin == 'd':
        direction.right()
      else:
        print('please input a w,a,s,d,stop,exit')

    '''
