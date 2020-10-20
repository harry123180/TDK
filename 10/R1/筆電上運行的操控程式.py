# 1 - Import library
import pygame
from pygame.locals import *
import math
import socket
import threading
from time import sleep
global packet
#########TCPIP設定##########
ClientSocket = socket.socket()
host = '25.7.170.68'
port = 1233
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
#####################
pls_nowr = 0
pls_nowl = 0
pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.

width, height = 64 * 10, 64 * 8
screen = pygame.display.set_mode((width, height))
player_x = 200
player_y = 200
keys = [False, False, False, False]
slection = 1
# 3 - Load images
up = pygame.image.load("up.png")
tomare = pygame.image.load("tomare.png")
left = pygame.image.load("left.png")
right = pygame.image.load("right2.png")
listA = [up, tomare, left, right]
###########################
mov_cmd = 0
mov_spd = 0
mov_dis = 0
#mov_cmd 運動指令 0 = 停 ;1 = 前 ;2 = 左 ; 3 = 右 ; 4 = 後
#mov_spd #速度設定
#mov_dis 移動距離/角度設定

###########################
Response = ClientSocket.recv(1024)
def read_server():
    while True:
        #Input = input('Say Something: ')
        Input = '0'+' '+str(mov_cmd) + ' ' + str(mov_spd) + ' ' + str (mov_dis)
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024).decode('utf-8')
        sult = Response.split(' ')
        print(sult)
        sleep(0.1)

# 4 - keep looping through
t = threading.Thread(target = read_server)
# 執行他
t.start()
while 1:

    # 5 - clear the screen before drawing it again
    screen.fill((255, 255, 255))
    # 6 - draw the screen elements
    slection = 1
    screen.blit(listA[slection], (player_x, player_y))


    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    mykeyslist = pygame.key.get_pressed()  # 获取按键元组信息
    mov_cmd = 0
    if mykeyslist[pygame.K_w]:  # 如果按键按下，这个值为1
        mov_cmd = 1
    elif mykeyslist[pygame.K_a]:  # 如果按键按下，这个值为1
        mov_cmd = 2
    elif mykeyslist[pygame.K_d]:  # 如果按键按下，这个值为1
        mov_cmd = 3
    elif mykeyslist[pygame.K_s]:  # 如果按键按下，这个值为1
        mov_cmd = 4
    elif mykeyslist[pygame.K_1]:
        mov_dis = 100
        print('set mov_dis = 100')
    elif mykeyslist[pygame.K_2]:
        mov_dis = 193
        print('set mov_dis = 193')
    elif mykeyslist[pygame.K_3]:
        mov_dis = 587
        print('set mov_dis = 587')
    elif mykeyslist[pygame.K_4]:
        mov_dis = 51
        print('set mov_dis = 51')
    elif mykeyslist[pygame.K_h]:
        mov_spd = 100
    elif mykeyslist[pygame.K_l]:
        mov_spd = 30
        print('CTRL')
    elif mykeyslist[pygame.K_p]:
        mov_dis = 1
        print('CTRL')
    elif mykeyslist[pygame.K_p]:
        mov_cmd =11
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)



ClientSocket.close()
t.join()
