# Importing the library
import math
import easygui
from time import sleep
import pygame
import all_func as FC
import pygame_gui
from khaibao import *
import numpy as np
# Initialing Color
# Initializing Pygame
pygame.init()
# Initializing surface
manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
#Toạ độ kết thúc của lưới toạ độ

surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
surface.fill(white_color) # đổi màu background sang trắng
pygame.display.set_caption('3D hình hộp chữ nhật') #Tên của sổ
background = pygame.Surface((manager_x,380))#Tạo phần điều khiển
background.fill(gray_black_color) #background của phần điều khiển

background1 = pygame.Surface((end_x+20,20))#Tạo phần điều khiển
background1.fill(white_color) #background của phần điều khiển

background2 = pygame.Surface((end_x+19,20))#Tạo phần điều khiển
background2.fill(white_color) #background của phần điều khiển

background3 = pygame.Surface((20,grid_y))#Tạo phần điều khiển
background3.fill(white_color) #background của phần điều khiển

background4 = pygame.Surface((19,grid_y))#Tạo phần điều khiển
background4.fill(white_color) #background của phần điều khiển
###################################
def clear_screen(isGrid):
    surface.fill(white_color) # đổi màu background sang trắng
    if(isGrid):
        FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
    FC.Draw_grid.xyz(surface,manager,start_x,end_x,start_y,end_y)
#############Phần điều khiển####################
bt_line = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,260,150,30),
                            text='Ve hinh',
                            manager=manager
                        )
X_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,20,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,20,40,30),
                            text="X",
                            manager=manager)
Y_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                            text="Y",
                            manager=manager)
Z_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,100,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,100,40,30),
                            text="Z",
                            manager=manager)
L_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,140,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,140,40,30),
                            text="Dai",
                            manager=manager)
W_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,180,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,180,40,30),
                            text="Rong",
                            manager=manager)
H_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,220,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,220,40,30),
                            text="Cao",
                            manager=manager)

bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,300,150,30),
                            text='Clear',
                            manager=manager
                        )
bt_grid = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,340,150,30),
                            text='Bat/Tat grid',
                            manager=manager
                        )

##################################################
isRunning = True
isGrid = False
clock = pygame.time.Clock()
FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
FC.Draw_grid.xyz(surface,manager,start_x,end_x,start_y,end_y)
while isRunning:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                try:
                    if event.ui_element == bt_line:
                        arr=[]
                        x=int(X_axis.get_text())
                        y=int(Y_axis.get_text())
                        z=int(Z_axis.get_text())
                        l=int(L_axis.get_text())
                        h=int(H_axis.get_text())
                        w=int(W_axis.get_text())
                        # A,B,C,D,E,F,G,H
                        # A(a1,a2)
                        # B(b1,b2)
                        #  ......
                        a1,a2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y,z)
                        b1,b2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y+h,z)
                        c1,c2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y+h,z)
                        d1,d2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y,z)
                        e1,e2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y,z+l)
                        f1,f2 = FC.Convert_coordinate.Chuyen_3Dto2D(x,y+h,z+l)
                        g1,g2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y+h,z+l)
                        h1,h2 = FC.Convert_coordinate.Chuyen_3Dto2D(x+w,y,z+l)

                        xA,yA = FC.Convert_coordinate.real2mon(a1,a2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('A', True, orange_color)
                        surface.blit(img, (xA+10, yA-20))
                        img = font.render("THONG SO", True, black_color)
                        surface.blit(img, (1050, 390))
                        toadoA = "%d,%d,%d" %(x,y,z)
                        img = font.render("A        " + toadoA, True, black_color)
                        surface.blit(img, (1050, 410))

                        xB,yB = FC.Convert_coordinate.real2mon(b1,b2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('B', True, orange_color)
                        surface.blit(img, (xB+10, yB-20))
                        toadoB = "%d,%d,%d" %(x,y+h,z)
                        img = font.render("B        " + toadoB, True, black_color)
                        surface.blit(img, (1050, 430))

                        xC,yC = FC.Convert_coordinate.real2mon(c1,c2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('C', True, orange_color)
                        surface.blit(img, (xC+10, yC-20))
                        toadoC = "%d,%d,%d" %(x+w,y+h,z)
                        img = font.render("C        " + toadoC, True, black_color)
                        surface.blit(img, (1050, 450))

                        xD,yD = FC.Convert_coordinate.real2mon(d1,d2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('D', True, orange_color)
                        surface.blit(img, (xD+10, yD-20))
                        toadoD = "%d,%d,%d" %(x+w,y,z)
                        img = font.render("D        " + toadoD, True, black_color)
                        surface.blit(img, (1050, 470))

                        xE,yE = FC.Convert_coordinate.real2mon(e1,e2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('E', True, orange_color)
                        surface.blit(img, (xE-20, yE+10))
                        toadoE = "%d,%d,%d" %(x,y,z+l)
                        img = font.render("E        " + toadoE, True, black_color)
                        surface.blit(img, (1050, 490))

                        xF,yF = FC.Convert_coordinate.real2mon(f1,f2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('F', True, orange_color)
                        surface.blit(img, (xF-20, yF+10))
                        toadoF = "%d,%d,%d" %(x,y+h,z+l)
                        img = font.render("F        " + toadoF, True, black_color)
                        surface.blit(img, (1050, 510))

                        xG,yG = FC.Convert_coordinate.real2mon(g1,g2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('G', True, orange_color)
                        surface.blit(img, (xG-20, yG+10))
                        toadoG = "%d,%d,%d" %(x+w,y+h,z+l)
                        img = font.render("G        " + toadoG, True, black_color)
                        surface.blit(img, (1050, 530))

                        xH,yH = FC.Convert_coordinate.real2mon(h1,h2)
                        font = pygame.font.SysFont(None, 24)
                        img = font.render('H', True, orange_color)
                        surface.blit(img, (xH-20, yH+10))
                        toadoH = "%d,%d,%d" %(x+w,y,z+l)
                        img = font.render("H        " + toadoH, True, black_color)
                        surface.blit(img, (1050, 550))

                        arr = FC.Draw.line(a1,a2,b1,b2,red_color,1)#AB
                        arr = np.concatenate((arr,FC.Draw.line(c1,c2,b1,b2,red_color)))#BC
                        arr = np.concatenate((arr,FC.Draw.line(c1,c2,d1,d2,red_color)))#CD
                        arr = np.concatenate((arr,FC.Draw.line(a1,a2,d1,d2,red_color,1)))#AD
                        arr = np.concatenate((arr,FC.Draw.line(a1,a2,e1,e2,red_color,1)))#AE
                        arr = np.concatenate((arr,FC.Draw.line(e1,e2,h1,h2,red_color)))#EH
                        arr = np.concatenate((arr,FC.Draw.line(d1,d2,h1,h2,red_color)))#DH
                        arr = np.concatenate((arr,FC.Draw.line(b1,b2,f1,f2,red_color)))#BF
                        arr = np.concatenate((arr,FC.Draw.line(f1,f2,g1,g2,red_color)))#FG
                        arr = np.concatenate((arr,FC.Draw.line(g1,g2,c1,c2,red_color)))#GC
                        arr = np.concatenate((arr,FC.Draw.line(e1,e2,f1,f2,red_color)))#EF
                        arr = np.concatenate((arr,FC.Draw.line(g1,g2,h1,h2,red_color)))#GH
                        arr = np.concatenate((arr,FC.Draw.line(d1,d2,c1,c2,red_color)))#DC

                        FC.Put_pixel(surface,arr)
                        FC.Put_pixel.point(surface,xA,yA,orange_color)
                        FC.Put_pixel.point(surface,xB,yB,orange_color)
                        FC.Put_pixel.point(surface,xC,yC,orange_color)
                        FC.Put_pixel.point(surface,xD,yD,orange_color)
                        FC.Put_pixel.point(surface,xE,yE,orange_color)
                        FC.Put_pixel.point(surface,xF,yF,orange_color)
                        FC.Put_pixel.point(surface,xG,yG,orange_color)
                        FC.Put_pixel.point(surface,xH,yH,orange_color)

                    if event.ui_element == bt_clear:
                        clear_screen(isGrid)
                    if event.ui_element == bt_grid:
                        isGrid = not(isGrid)
                        clear_screen(isGrid)
                except ValueError:
                    easygui.msgbox("X and Y not be empty", title="ERROR")
        manager.process_events(event)
    surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ
    surface.blit(background1,(0,0))#thanh bên trên
    surface.blit(background2,(0,grid_y+21))#thanh bên dưới
    surface.blit(background3,(0,20))#thanh bên trái
    surface.blit(background4,(grid_x+21,20))#thanh bên phải
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.flip()
    # clear_screen(isGrid)