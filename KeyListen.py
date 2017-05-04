import pygame, sys
import numpy as np
import pandas as pd
import serial

white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
pygame.display.set_caption('Keyboard Example')
size = [640, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ser = serial.Serial('/dev/ttyUSB0', 9600)  # Establish the connection on a specific port

pygame.key.set_repeat(50, 50)
counter = 0
k = [0]

DataArray = []

while True:
    del k[:]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # check if key is pressed
        # if you use event.key here it will give you error at runtime
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                k = [1]  # x+
            if event.key == pygame.K_LEFT:
                k = [2]  # x-
            if event.key == pygame.K_UP:
                k = [3]  # y+
            if event.key == pygame.K_DOWN:
                k = [4]  # y-
            if (event.key == pygame.K_KP5) or (event.key == pygame.K_5):
                k = [5]  # z+
            if (event.key == pygame.K_KP6) or (event.key == pygame.K_6):
                k = [6]  # z-

            if (event.key == pygame.K_p):
                print "HelloHai"
                print DataArray
                mat = np.column_stack(DataArray)
                qwer = pd.DataFrame({"x": mat[0], "y": mat[1], "z": mat[2], "Direction": mat[3]})
                print qwer

                writer = pd.ExcelWriter(
                    '/home/pavan/PAVANKUMAR/MachineLearning/MyFolder/DataFiles/accelero_data.xlsx',
                    engine='xlsxwriter')
                qwer.to_excel(writer, 'accFile')
                writer.save()

                sys.exit()
                # Quit and frame the data

    SerialDat = ser.readline()
    # print k, ar
    # Q = np.random.rand(1,3)
    Z = [df.strip() for df in SerialDat.split(',')]
    if len(k) != 0:
        print Z + k
        DataArray.append(Z + k)

    else:
        print SerialDat

    # print Z + k
    # print np.append(SerialDat, k)
    # t.sleep(.1)

    # pygame.draw.rect(screen, red, ((x, y), (step, step)), 0)

    # pygame.display.update()
    clock.tick(20)
