import easygui
import pygame
import all_func as PX
import pygame_gui
from khaibao import *
# Initializing Pygame
pygame.init()
surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
surface.fill(white_color) # đổi màu background sang trắng
pygame.display.set_caption('BT1') #Tên của sổ
background = pygame.Surface((manager_x,end_y+20))#Tạo phần điều khiển
background.fill(gray_black_color) #background của phần điều khiển
manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
#######################################################################################
def draw_grid(start_x,end_x,start_y,end_y):
    #vẽ đƯờng ngang
    for x in range(start_x,end_x+UNIT,UNIT):
        pygame.draw.line(surface,gray_color,(x,start_x),(x,end_y))
    #vẽ đường dọc
    for y in range(start_y,end_y+UNIT,UNIT):
        pygame.draw.line(surface,gray_color,(start_y,y),(end_x,y))
    #vẽ trục toạ độ
    for x in range(start_y,end_y,UNIT): #vẽ trục y
        PX.Put_pixel(surface,(end_x+start_x)/2,x,gray_color)
    for x in range(start_x,end_x,UNIT): #vẽ trục y
        PX.Put_pixel(surface,x,(end_y+start_y)/2,gray_color)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(500,0,40,20),
                            text="Y",
                            manager=manager)
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(990,300,40,20),
                        text="X",
                        manager=manager)
def clear_screen():
    surface.fill(white_color) # đổi màu background sang trắng
    draw_grid(start_x,end_x,start_y,end_y) # vẽ lưới toạ độ

def ve8diem(x0,y0,x,y):
    PX.Put_pixel.revert(surface,x0 + x , y0 + y ,red_color)
    PX.Put_pixel.revert(surface,x0 - x , y0 + y ,red_color)
    PX.Put_pixel.revert(surface,x0 + x , y0 - y ,red_color)
    PX.Put_pixel.revert(surface,x0 - x , y0 - y ,red_color)
    PX.Put_pixel.revert(surface,x0 + x , y0 + y ,red_color)
    PX.Put_pixel.revert(surface,x0 + y , y0 + x ,red_color)
    PX.Put_pixel.revert(surface,x0 - y , y0 + x ,red_color)
    PX.Put_pixel.revert(surface,x0 + y , y0 - x ,red_color)
    PX.Put_pixel.revert(surface,x0 - y , y0 - x ,red_color)
def draw_circle(x0,y0,r,dash):
    x=0
    y=r
    p=3-2*r
    count=0
    while (x<=y):
        if(count%dash!=0):
            ve8diem(x0,y0,x,y)
        count+=1
        if(p<0):
            p=p+4*x+6
        else:
            p=p+4*(x-y)+10
            y=y-1
        x=x+1
###################################################################
bt_draw = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,100,150,30),
                            text='Ve hinh tron',
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
R = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+30,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis,60,40,30),
                            text="R",
                            manager=manager)
Dash = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(manager_x_axis+110,60,40,30),
                            manager=manager)
pygame_gui.elements.UILabel(relative_rect=pygame.Rect(manager_x_axis+75,60,40,30),
                            text="Dash",
                            manager=manager)
bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,350,150,30),
                            text='Clear',
                            manager=manager
                        )
##################################################
isRunning = True
clock = pygame.time.Clock()
draw_grid(start_x,end_x,start_y,end_y) # vẽ lưới toạ độ

while isRunning:
    time_delta = clock.tick(60)/1000.0
    surface.blit(background,(manager_x_axis,0))#ghi đè lên cửa sổ

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                try:
                    if event.ui_element == bt_draw:
                        x=int(X1_axis.get_text())
                        y=int(Y1_axis.get_text())
                        r=int(R.get_text())
                        dash=int(Dash.get_text()) 
                        draw_circle(x,y,r,dash)
                except ValueError:
                    easygui.msgbox("X and Y not be empty", title="ERROR")
                if event.ui_element == bt_clear:
                    clear_screen()
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.update()