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
    # pygame.draw.rect(surface,red_color,pygame.Rect(0, 0, 1000, 600))
    FC.Draw_grid(surface,manager,start_x,end_x,start_y,end_y)
    FC.Draw_grid.xy(surface,manager,start_x,end_x,start_y,end_y)
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
FC.Draw_grid.xy(surface,manager,start_x,end_x,start_y,end_y)
#################################### DORAEMON #######################################
face= FC.Draw.ellipse_2(20,20,blue_color,0,140)
face = np.concatenate((face,FC.Draw.ellipse_2(20,20,black_color,220,335),FC.Draw.ellipse_2(20,20,blue_color,336,360),FC.Draw.rect(-12,-16,12,-18,red_color)))
mat = FC.Draw.ellipse_2(20,25,blue_color,35,125)
mat = FC.Bien_doi.Nhan_MT(mat,FC.Bien_doi.MT_tinh_tien(-100,20))
eye = FC.Draw.ellipse_2(3,5,black_color,40,230)
eye = FC.Bien_doi.phep_quay(eye,0,0,20)
eye = FC.Bien_doi.Nhan_MT(eye,FC.Bien_doi.MT_tinh_tien(-50,-75))
x_eye,y_eye = FC.Convert_coordinate.real2mon(-11,14)
dau = np.concatenate((face,mat,eye,[[x_eye,y_eye,black_color]]))
dau = FC.Bien_doi.phep_quay(dau,0,0,-20)
mui = FC.Draw.circle_fill(-19,8,2,red_color,red_color)
mong = FC.Draw.ellipse_2(20,15,blue_color,25,80)
mong = FC.Bien_doi.Nhan_MT(mong,FC.Bien_doi.MT_tinh_tien(50,140))
bung = FC.Draw.ellipse_2(20,15,black_color,180,300)
bung = FC.Bien_doi.Nhan_MT(bung,FC.Bien_doi.MT_tinh_tien(70,140))
chan = FC.Draw.line(15,-43,30,-42,blue_color)
chan = np.concatenate((chan,FC.Draw.line(30,-25,32,-26,blue_color),FC.Draw.ellipse_fill(35,-35,6,8,black_color,white_color)))
chuong = FC.Draw.circle_fill(-6,-20,2,yellow_color,yellow_color)
tay = FC.Draw.line(3,-21,8,-14,black_color)
tay = np.concatenate((tay,FC.Draw.line(13,-24,15,-17,black_color),FC.Draw.circle_fill(13,-13,4,black_color,white_color)))
bung_duoi = FC.Draw.ellipse_2(20,15,black_color,0,100)
bung_duoi = FC.Bien_doi.Nhan_MT(bung_duoi,FC.Bien_doi.MT_tinh_tien(-25,200))
tui = FC.Draw.ellipse_2(8,8,black_color,30,100)
tui = FC.Bien_doi.Nhan_MT(tui,FC.Bien_doi.MT_tinh_tien(0,200))
tui = np.concatenate((tui,FC.Draw.line(0,-37,4,-33,black_color)))
duoi = np.concatenate((FC.Draw.circle_fill(36,-18,2,red_color,red_color),FC.Draw.line(33,-20,30,-22,black_color)))
chong_chong = FC.Draw.ellipse_2(3,3,yellow_color,0,120)
chong_chong = np.concatenate((chong_chong,FC.Draw.ellipse_2(3,3,yellow_color,270,360)))
chong_chong = FC.Bien_doi.Nhan_MT(chong_chong,FC.Bien_doi.MT_tinh_tien(30,-100))
chong_chong = np.concatenate((chong_chong,FC.Draw.line(7,23,8,28,yellow_color)))
canh_quat = FC.Draw.ellipse_2(6,3,black_color,0,360)
canh_quat = FC.Bien_doi.phep_quay(canh_quat,0,0,10)
canh_quat = FC.Bien_doi.Nhan_MT(canh_quat,FC.Bien_doi.MT_tinh_tien(40,-140))
chong_chong = np.concatenate((chong_chong,canh_quat))
mieng = FC.Draw.ellipse_2(10,10,black_color,90,160)
mieng = FC.Bien_doi.Nhan_MT(mieng,FC.Bien_doi.MT_tinh_tien(-90,20))
chi_tiet_mat = np.concatenate((mui,mieng,FC.Draw.line(-8,0,1,6,black_color),FC.Draw.line(-5,-3,5,2,black_color),FC.Draw.line(-4,-6,5,-4,black_color),chuong,chong_chong))
phan_than = np.concatenate((mong,bung,chan,duoi,bung_duoi))
linh_kien = np.concatenate((tui,tay))
doraemon = np.concatenate((dau,phan_than,linh_kien,chi_tiet_mat))
#################################### MAY #######################################
may = FC.Draw.ellipse_2(6,5,pink_dark_color,0,120)
may = FC.Bien_doi.Nhan_MT(may,FC.Bien_doi.MT_tinh_tien(0,25))
may1 = FC.Draw.ellipse_2(12,12,pink_dark_color,0,160)
may1 = FC.Bien_doi.Nhan_MT(may1,FC.Bien_doi.MT_tinh_tien(25,100))
may2 = FC.Draw.ellipse_2(8,8,pink_dark_color,80,180)
may2 = FC.Bien_doi.Nhan_MT(may2,FC.Bien_doi.MT_tinh_tien(0,160))
may = np.concatenate((may,may1,may2,FC.Draw.line(0,0,0,-40,pink_dark_color)))
may = FC.Bien_doi.phep_quay(may,0,0,-90)
FC.Put_pixel(surface,may)
a,b = FC.Convert_coordinate.real2mon(20,3)
FC.To_mau.loang(surface,a,b,pink_dark_color,pink_color,may)
# FC.Put_pixel(surface,doraemon)
count =0
bool = 5
while isRunning:
    time_delta = clock.tick(60)/1000.0
    surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ
    # face = np.concatenate((face,FC.Dr))
    # a,b = FC.Convert_coordinate.real2mon(0,0)
    # mt=np.dot(FC.Bien_doi.MT_tinh_tien(-a,-b),FC.Bien_doi.MT_quay(-20))
    # mt=np.dot(mt,FC.Bien_doi.MT_tinh_tien(a,b))
    # face = FC.Bien_doi.Nhan_MT(face,mt)
    count +=1
    if (count>10):
        bool = -bool
        count =0
    doraemon = FC.Bien_doi.Nhan_MT(doraemon,FC.Bien_doi.MT_tinh_tien(0,bool))
    FC.Put_pixel(surface,doraemon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # try:
                    if event.ui_element == bt_line:
                        ox,oy = FC.Convert_coordinate.real2mon(0,0)
                        mt_bien_doi = np.dot(FC.Bien_doi.MT_tinh_tien(-ox,-oy),FC.Bien_doi.MT_doi_xung(2))
                        mt_bien_doi = np.dot(mt_bien_doi,FC.Bien_doi.MT_tinh_tien(ox,oy))
                        doraemon = FC.Bien_doi.Nhan_MT(doraemon,mt_bien_doi)
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
                # except ValueError:
                #     easygui.msgbox("X and Y not be empty", title="ERROR")
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.flip()
    clock.tick(24)
    clear_screen()
