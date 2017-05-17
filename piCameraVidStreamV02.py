# @file piCamVidStreamV02.py
#
# @brief This is a server which broadcasts h264 video stream
#
# On the client side for Windows, run vlc on the cmd prompt:
# "C:\Program Files (x86)\VideoLAN\VLC\vlc" tcp/h264://192.168.1.105:8000
# and change the IP address to that of the pi
#
# Source: Raspberry Pi camera documentation
#
# Created for Python 3
# Created 16 May 2017
#
# @author Mustafa Ghazi

import socket
import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

print('Attempting to start camera broadcast\n')

server_socket = socket.socket()
server_socket.bind(('0.0.0.0',8000))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('wb')
try:
    camera.start_recording(connection, format='h264')
    camera.wait_recording(120)
    camera.stop_recording()
finally:
    connection.close()
    server_socket.close()
    camera.close()

print('End of camera broadcast\nGoodbye!')



