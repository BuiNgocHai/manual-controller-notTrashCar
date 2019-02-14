#!/usr/bin/python3
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

import json
from config import *
import controller

try:
    os.chdir(os.path.dirname(__file__))
    os.system('clear')
    print("\nWait for initial setup, please don't connect anything yet...\n")
    sys.path.remove('/opt/ros/lunar/lib/python2.7/dist-packages')
except:
    pass

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video_out_name = 'output_{}.avi'.format(time.time())
# video_out = cv2.VideoWriter(video_out_name, fourcc, 20, (320, 240))

speeds = []
angles = []

def car_control(angle, speed):
 
    pub_speed = rospy.Publisher('/team705_speed', Float32, queue_size=10)
    pub_speed.publish(speed)
    pub_angle = rospy.Publisher('/team705_steerAngle', Float32, queue_size=10)
    pub_angle.publish(angle)
    print('Angle:', angle, 'Speed:', speed)
    speeds.append(speed)
    angles.append(angle)

# def getch():
#     fd = sys.stdin.fileno()
#     old_setting = termios.tcgetattr(fd)
#     tty.setraw(sys.stdin.fileno())
#     ch = sys.stdin.read(1)
#     termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
#     return ch

def image_callback(data):
    start_time = time.time()
    #controller.RCTest()
    temp = np.fromstring(data.data, np.uint8)
    img = cv2.imdecode(temp, cv2.IMREAD_COLOR)
    cv2.imshow('raw_frame', img)
    
    wirte_data(img,start_time )
    
    
    # video_out.write(img)
    cv2.waitKey(1)
    #rint('FPS:', 1/(time.time() - start_time))

def wirte_data(img,img_index):
    #print('speed_now: ',speeds[-1])
    img_name = str(img_index)+'_'+str(angles[-1])+'_'+ str(speeds[-1]) +'.jpg'
    cv2.imwrite(img_path+ img_name,img)
    #lables
    image_infor = {}
    image_infor[img_name] = []
    image_infor[img_name].append({
        #'index': image_count,
        'path': img_path+img_name,
        'speed': speeds[-1],
        'angle': angles[-1] 
        #'keyboard_status': keyboard_status + '\n'
    })  
    
    with open(img_path + 'labels.json','a', encoding='utf-8') as lables_file:  
        json.dump(image_infor, lables_file, ensure_ascii=False, sort_keys=False, indent=4)
        lables_file.write("\n")
    

def main():
    
    rospy.init_node('team705_node', anonymous=True)
    # rospy.Subscriber("/team705_image/compressed", CompressedImage,
    #                  image_callback, queue_size=1, buff_size=2**24)
    controller.RCTest()
    rospy.spin()
    
    # video_out.release()
    # print('Saved', video_out_name)


if __name__ == '__main__':
    main()
