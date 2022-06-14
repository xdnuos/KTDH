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
pygame.display.set_caption('do an cuoi ki') #Tên của sổ
background = pygame.Surface((manager_x,end_y+20))#Tạo phần điều khiển
background.fill(gray_black_color) #background của phần điều khiển
###################################
def clear_screen():
    surface.fill(white_color) # đổi màu background sang trắng
    FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
#############Phần điều khiển####################
bt_line = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,240,150,30),
                            text='Duong thang',
                            manager=manager
                        )
X_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,20,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,20,40,30),
                            text="X",
                            manager=manager)
Y_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+110,20,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+80,20,40,30),
                            text="Y",
                            manager=manager)
Z_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                            text="Z",
                            manager=manager)
L_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,100,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,100,40,30),
                            text="Dai",
                            manager=manager)
W_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,140,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,140,40,30),
                            text="Rong",
                            manager=manager)
H_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+60,180,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+10,180,40,30),
                            text="Cao",
                            manager=manager)

# bt_dash = pygame_gui.elements.UIButton(
#                             relative_rect=pygame.Rect(manager_x_axis+5,140,150,30),
#                             text='Net dut',
#                             manager=manager
#                         )
# bt_dash_dot = pygame_gui.elements.UIButton(
#                             relative_rect=pygame.Rect(manager_x_axis+5,180,150,30),
#                             text='Net cham gach',
#                             manager=manager
#                         )
# bt_dash_dash_dot = pygame_gui.elements.UIButton(
#                             relative_rect=pygame.Rect(manager_x_axis+5,220,150,30),
#                             text='Hai cham gach',
#                             manager=manager
#                         )
# bt_arrow = pygame_gui.elements.UIButton(
#                             relative_rect=pygame.Rect(manager_x_axis+5,260,150,30),
#                             text='Net mui ten',
#                             manager=manager
#                         )
# bt_rect = pygame_gui.elements.UIButton(
#                             relative_rect=pygame.Rect(manager_x_axis+5,300,150,30),
#                             text='Hinh chu nhat',
#                             manager=manager
#                         )
bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,350,150,30),
                            text='Clear',
                            manager=manager
                        )
##################################################
isRunning = True
clock = pygame.time.Clock()
FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
FC.Draw_grid.xyz(surface,manager,start_x,end_x,start_y,end_y)
while isRunning:
    time_delta = clock.tick(60)/1000.0
    surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ

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

                        arr = FC.Draw.line(a1,a2,b1,b2,red_color,1)#AB
                        arr = np.concatenate((arr,FC.Draw.line(c1,c2,b1,b2,red_color)))#BC
                        arr = np.concatenate((arr,FC.Draw.line(c1,c2,d1,d2,red_color)))#CD
                        arr = np.concatenate((arr,FC.Draw.line(a1,a2,d1,d2,red_color,1)))#AD

                        FC.Put_pixel(surface,arr)
                    # if event.ui_element == bt_dash:
                    #     x1=int(X1_axis.get_text())
                    #     y1=int(Y1_axis.get_text())
                    #     x2=int(X2_axis.get_text())
                    #     y2=int(Y2_axis.get_text())
                    #     FC.Draw.line(surface,x1,y1,x2,y2,red_color,1)
                    # if event.ui_element == bt_dash_dot:
                    #     x1=int(X1_axis.get_text())
                    #     y1=int(Y1_axis.get_text())
                    #     x2=int(X2_axis.get_text())
                    #     y2=int(Y2_axis.get_text())
                    #     FC.Draw.line(surface,x1,y1,x2,y2,red_color,2)
                    # if event.ui_element == bt_dash_dash_dot:
                    #     x1=int(X1_axis.get_text())
                    #     y1=int(Y1_axis.get_text())
                    #     x2=int(X2_axis.get_text())
                    #     y2=int(Y2_axis.get_text())
                    #     FC.Draw.line(surface,x1,y1,x2,y2,red_color,3)
                    # if event.ui_element == bt_arrow:
                    #     x1=int(X1_axis.get_text())
                    #     y1=int(Y1_axis.get_text())
                    #     x2=int(X2_axis.get_text())
                    #     y2=int(Y2_axis.get_text())
                    #     FC.Draw.line(surface,x1,y1,x2,y2,red_color,0)
                    #     FC.Draw.arrow(surface,x1,y1,x2,y2,red_color)
                    # if event.ui_element == bt_rect:
                    #     x1=int(X1_axis.get_text())
                    #     y1=int(Y1_axis.get_text())
                    #     x2=int(X2_axis.get_text())
                    #     y2=int(Y2_axis.get_text())
                    #     FC.Draw.rect(surface,x1,y1,x2,y2,red_color)
                        # FC.Draw.ellipse(surface,x1,y1,x2,y2,red_color)
                    if event.ui_element == bt_clear:
                        clear_screen()
                except ValueError:
                    easygui.msgbox("X and Y not be empty", title="ERROR")
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.update()
    # clear_screen()