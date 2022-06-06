# Importing the library
import math
import easygui
from time import sleep
import pygame
import all_func as FC
import pygame_gui
from khaibao import *
# Initialing Color
# Initializing Pygame
pygame.init()
# Initializing surface
manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
#Toạ độ kết thúc của lưới toạ độ

surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
surface.fill(white_color) # đổi màu background sang trắng
pygame.display.set_caption('BT1') #Tên của sổ
background = pygame.Surface((manager_x,end_y+20))#Tạo phần điều khiển
background.fill(gray_black_color) #background của phần điều khiển
###################################
def clear_screen():
    surface.fill(white_color) # đổi màu background sang trắng
    FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
#############Phần điều khiển####################
bt_line = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,100,150,30),
                            text='Duong thang',
                            manager=manager
                        )
X1_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,20,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,20,40,30),
                            text="X1",
                            manager=manager)
Y1_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+110,20,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+80,20,40,30),
                            text="Y1",
                            manager=manager)
X2_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                            text="X2",
                            manager=manager)
Y2_axis = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+110,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+80,60,40,30),
                            text="Y2",
                            manager=manager)
bt_dash = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,140,150,30),
                            text='Net dut',
                            manager=manager
                        )
bt_dash_dot = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,180,150,30),
                            text='Net cham gach',
                            manager=manager
                        )
bt_dash_dash_dot = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,220,150,30),
                            text='Hai cham gach',
                            manager=manager
                        )
bt_arrow = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,260,150,30),
                            text='Net mui ten',
                            manager=manager
                        )
bt_rect = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,300,150,30),
                            text='Hinh chu nhat',
                            manager=manager
                        )
bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,350,150,30),
                            text='Clear',
                            manager=manager
                        )
##################################################
isRunning = True
clock = pygame.time.Clock()
FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y) # vẽ lưới toạ độ
while isRunning:
    time_delta = clock.tick(60)/1000.0
    surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # try:
                    if event.ui_element == bt_line:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.draw_line(surface,x1,y1,x2,y2,0)
                    if event.ui_element == bt_dash:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.draw_line(surface,x1,y1,x2,y2,1)
                    if event.ui_element == bt_dash_dot:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.draw_line(surface,x1,y1,x2,y2,2)
                    if event.ui_element == bt_dash_dash_dot:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.draw_line(surface,x1,y1,x2,y2,3)
                    if event.ui_element == bt_arrow:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.draw_line(surface,x1,y1,x2,y2)
                        FC.Draw.draw_arrow(surface,x1,y1,x2,y2)
                    if event.ui_element == bt_rect:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        FC.Draw.rect(surface,x1,y1,x2,y2,red_color)
                # except ValueError:
                #     easygui.msgbox("X and Y not be empty", title="ERROR")
                    if event.ui_element == bt_clear:
                        clear_screen()
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.update()
    # clear_screen()