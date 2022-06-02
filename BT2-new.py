# Importing the library
import math
import easygui
from time import sleep
import pygame
import putpixel as PX
import pygame_gui
from khaibao import *
import convert_pixel as CV
# Initialing Color
# Initializing Pygame
pygame.init()
# Initializing surface
#Toạ độ kết thúc của lưới toạ độ

surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ #1180x620
surface.fill(white_color) # đổi màu background sang trắng
pygame.display.set_caption('BT1') #Tên của sổ
background = pygame.Surface((manager_x,end_y+20))#Tạo phần điều khiển
background.fill(gray_black_color) #background của phần điều khiển
manager = pygame_gui.UIManager((end_x+manager_x,end_y+20))
###################################
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
def PutPX(count,x,y,type):
    match type:
        case 1:
            if(count%3!=0):
                PX.Put_pixel.revert(surface,x,y,red_color)
        case 2:
            global dash_dot
            if(count%5!=0 and count!= dash_dot):
                PX.Put_pixel.revert(surface,x,y,red_color)
            if(count==dash_dot):
                dash_dot +=5
        case 3:
            global dash_dash_dot
            if(count%7!=0 and count!= dash_dash_dot):
                PX.Put_pixel.revert(surface,x,y,red_color)
            if(count==dash_dash_dot):
                dash_dash_dot+=7
        case default:
            PX.Put_pixel.revert(surface,x,y,red_color)
def draw_arrow(x1,y1,x2,y2):
        Dx = (x2 - x1)
        Dy = (y2 - y1)
        arrowLength = round(math.sqrt(Dx ** 2 + Dy ** 2) / 6)
        if (arrowLength < 3):
            arrowLength = 3
        angle = math.atan2(Dy, Dx)
        x1_new = round(x2 - arrowLength * math.cos(angle - math.pi / 6))
        y1_new = round(y2 - arrowLength * math.sin(angle - math.pi / 6))
        x2_new = round(x2 - arrowLength * math.cos(angle + math.pi / 6))
        y2_new = round(y2 - arrowLength * math.sin(angle + math.pi / 6))

        draw_line(x2, y2, x1_new, y1_new)
        draw_line(x2, y2, x2_new, y2_new)
def draw_line(x1,y1,x2,y2,type=0):
    ############## Sử dụng để vẽ nét đứt ###############
    #khai báo biến toàn cục
    global dash_dot
    global dash_dash_dot
    count=1
    ############## END #################################
    ############## Thuật toán vẽ đường thẳng khi các đường thẳng đứng hoặc nằm ngang ############
    x = x1
    y = y1
    PX.Put_pixel.revert(surface,x,y,red_color)# vẽ điểm đầu tiên
    xUNIT = 1
    yUNIT = 1; 
    #xét trường hợp để cho yUNIT và xUNIT để vẽ tăng lên hay giảm xuống
    if (x2 - x1 < 0):
        xUNIT = -xUNIT
    if (y2 - y1 < 0):
        yUNIT = -yUNIT
    if (x1 == x2):   # trường hợp vẽ đường thẳng đứng
        while (y != y2):
            y += yUNIT
            count+=1
            PutPX(count,x,y,type)
 
    elif (y1 == y2):  #trường hợp vẽ đường ngang
        while (x != x2):
            x += xUNIT
            count+=1
            PutPX(count,x,y,type)
    ##################### END #############################################
    else:          # trường hợp vẽ các đường xiên -> sử dụng thuật toán bresenham
    #########Thuật toán Bresenham vẽ đường thẳng##############
    # Trường hợp hệ số góc 0 < m <= 1:
    # P = 2dy – dx
    # nếu P >= 0 y++; P = P + (2dy – 2dx);
    # còn lại P = P + 2dy;

    # Trường hợp hệ số góc -1<= m < 0:
    # P = 2dy + dx
    # nếu P < 0 thì y–; P = P + (2dy + 2dx);
    # còn lại P = P + 2dy;

    # Trường hợp hệ số góc m > 1:
    # P = 2dx – dy
    # nếu P >=0 thì x++; P = P + (2dx – 2dy);
    # còn lại P = P + 2dx;

    # Trường hợp hệ số góc nhỏ m > -1:
    # P = 2dx + dy
    # nếu P < 0 thì x–; P = P+ (2dx + 2dy);
    # còn lại P = P + 2dx;

    #vì sử dụng trị tuyệt đối cho Dx và Dy nên loại bỏ 2 trường hợp m>-1 và -1<= m < 0
    #############################################
        Dx = abs(x2 - x1)
        Dy = abs(y2 - y1)
        m=Dy/Dx # trường hợp Dx = 0 đã được vẽ (đường thẳng đứng) 
        if(m>1):
            p=2*Dx-Dy
            while(x != x2):
                if (p<0) :
                    p += 2*Dx
                else:
                    p += 2*(Dx-Dy)
                    x += xUNIT
                y += yUNIT
                count+=1
                PutPX(count,x,y,type)
        else:
            p = 2*Dy - Dx
            while(x != x2):
                if (p<0) :
                    p += 2*Dy
                else:
                    p += 2*(Dy-Dx)
                    y += yUNIT
                x += xUNIT
                count+=1
                PutPX(count,x,y,type)
    #trả lại giá trị ban đầu
    dash_dot=3
    dash_dash_dot=5
def clear_screen():
    surface.fill(white_color) # đổi màu background sang trắng
    draw_grid(start_x,end_x,start_y,end_y) # vẽ lưới toạ độ
def drar_rect(x1,y1,x2,y2):
    x_max=x1
    y_max=y1
    x_min=x2
    y_min=y2
    if(x2>x1):
        x_max=x2
        x_min=x1
    if(y2>y1):
        y_max=y2
        y_min=y1
    for x in range(x_max-x_min):
        for y in range(y_max-y_min):
            PX.Put_pixel.revert(surface,x,y,red_color)
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
                    if event.ui_element == bt_line:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2)
                    if event.ui_element == bt_dash:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2,1)
                    if event.ui_element == bt_dash_dot:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2,2)
                    if event.ui_element == bt_dash_dash_dot:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2,3)
                    if event.ui_element == bt_arrow:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2)
                        draw_arrow(x1,y1,x2,y2)
                    if event.ui_element == bt_rect:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        drar_rect(x1,y1,x2,y2)
                except ValueError:
                    easygui.msgbox("X and Y not be empty", title="ERROR")
                if event.ui_element == bt_clear:
                    clear_screen()
        manager.process_events(event)
    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.update()
    # clear_screen()