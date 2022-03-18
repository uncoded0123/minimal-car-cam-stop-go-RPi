import pygame.camera
import numpy as np
import RPi.GPIO as GPIO
out_board_pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(out_board_pin, GPIO.OUT)
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (960, 720)) #width,height, 
cam.start()
def convert_to_bw():
    imarr = int(pygame.surfarray.array3d(cam.get_image()).mean())
    if imarr < 100:
        GPIO.output(out_board_pin, GPIO.LOW)
    elif imarr >= 100:
        GPIO.output(out_board_pin, GPIO.HIGH)
while 1:
    convert_to_bw()
    pygame.time.delay(100)
cam.stop()
pygame.quit()
