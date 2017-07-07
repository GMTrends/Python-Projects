#joystick_fun.py
# This script allows to interact with the joystick sensor on the Raspberry Pi

import pygame
from pygame.locals import *
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    start_monitor(sense)

def start_monitor(sense):
    x = 0
    y = 0
    points_list = []
    for i in range(0,64):
        points_list.append([0,0,0])
    points_list[0] = [255,255,255]
    sense.set_pixels(points_list)
    try:
        pygame.init()
        pygame.display.set_mode((1,1))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if y <= 6:
                            y = y + 1
                            position = x + 8 * y
                            points_list[position] = [255,255,255]
                    elif event.key == pygame.K_UP:
                        if y >= 1:
                            y = y - 1
                            position = x + 8 * y
                            points_list[position] = [255,255,255]
                    elif event.key == pygame.K_RIGHT:
                        if x <= 6:
                            x = x + 1
                            position = x + 8 * y
                            points_list[position] = [255,255,255]
                    elif event.key == pygame.K_LEFT:
                        if x >= 1:
                            x = x - 1
                            position = x + 8 * y
                            points_list[position] = [255,255,255]
                    else:
                        running = False
                        break
                sense.set_pixels(points_list)
    except KeyboardInterrupt:
        print("Exiting...")
        pygame.quit()
    finally:
        sense.clear()
    sleep(0.1)
    sense.clear()
    
main()
