import serial
import pygame
from pygame.locals import *
import main
import os
import sys
import time

import cv2
import numpy as np

import rospkg
import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import Float32


import sys
import termios
import tty
class RCTest(object):
    
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((250, 250))
        self.send_inst = True
        self.steer()

    def steer(self):
        
        while self.send_inst:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        main.car_control(angle = 10,speed=50)

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print("Forward Left")
                        main.car_control(angle = -10,speed=50)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print("Reverse Right")
                        main.car_control(angle = 190,speed=50)

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print("Reverse Left")
                        main.car_control(angle = 170,speed=50)

                    elif key_input[pygame.K_UP]:
                        print("Forward")
                        main.car_control(angle = 0,speed=150)

                    elif key_input[pygame.K_DOWN]:
                        print("Reverse")
                        main.car_control(angle = 180,speed=50)

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        main.car_control(angle = 20,speed=10)

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        main.car_control(angle = -20,speed=50)
                    
                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print("Exit")
                        self.send_inst = False
                        break
                    rospy.Subscriber("/team705_image/compressed", CompressedImage,
                     main.image_callback, queue_size=1, buff_size=2**24)
                else:
                    main.car_control(angle = 0, speed = 0)


