# Importing the library
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


surface = pygame.display.set_mode((end_x+manager_x,end_y+20)) #tạo cửa sổ
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
def PutPX(count,x,y,type):
    match type:
        case 1:
            if(count%3!=0):
                PX.Put_pixel.revert(surface,x,y,red_color)
        case 2:
            if(count%5!=0):
                PX.Put_pixel.revert(surface,x,y,red_color)
        case 3:
            if(count%7!=0):
                PX.Put_pixel.revert(surface,x,y,red_color)
        case default:
            PX.Put_pixel.revert(surface,x,y,red_color)

def draw_line(x1,y1,x2,y2,type=2):
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
    count=1
    Dx = abs(x2 - x1)
    Dy = abs(y2 - y1)
    m=0
    if(Dx!=0):
        m=Dy/Dx # hệ số góc
    cross=0 #0<m<1
    if(m>1):
        p=2*Dx-Dy
        cross=1#m>1
    elif(m>=0 and m<=1):
        p = 2*Dy - Dx
    x = x1
    y = y1
 
    xUNIT = 1
    yUNIT = 1; 
    #xét trường hợp để cho yUNIT và xUNIT để vẽ tăng lên hay giảm xuống
    if (x2 - x1 < 0):
        xUNIT = -xUNIT
    if (y2 - y1 < 0):
        yUNIT = -yUNIT
 
    if (x1 == x2):   # trường hợp vẽ đường thẳng đứng
        PX.Put_pixel.revert(surface,x,y,red_color)# vẽ điểm đầu tiên
        while (y != y2+1):
            count+=1
            y += yUNIT
            PutPX(count,x,y,type)
 
    elif (y1 == y2):  #trường hợp vẽ đường ngang
        PX.Put_pixel.revert(surface,x,y,red_color)# vẽ điểm đầu tiên
        while (x != x2+1):
            x += xUNIT
            PX.Put_pixel.revert(surface,x,y,red_color)
            
    else:          # trường hợp vẽ các đường xiên
        PX.Put_pixel.revert(surface,x,y,red_color)
        while(x != x2):
            if(cross):
                if (p<0) :
                    p += 2*Dx
                else:
                    p += 2*(Dx-Dy)
                    x += xUNIT
                y += yUNIT
            else:
                if (p<0) :
                    p += 2*Dy
                else:
                    p += 2*(Dy-Dx)
                    y += yUNIT
                x += xUNIT
            PX.Put_pixel.revert(surface,x,y,red_color)

def clear_screen():
    surface.fill(white_color) # đổi màu background sang trắng
    draw_grid(start_x,end_x,start_y,end_y) # vẽ lưới toạ độ

#############Phần điều khiển####################
bt_line = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,100,150,30),
                            text='Draw Line',
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
bt_clear = pygame_gui.elements.UIButton(
                            relative_rect=pygame.Rect(manager_x_axis+5,150,150,30),
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
                if event.ui_element == bt_line:
                    try:
                        x1=int(X1_axis.get_text())
                        y1=int(Y1_axis.get_text())
                        x2=int(X2_axis.get_text())
                        y2=int(Y2_axis.get_text())
                        draw_line(x1,y1,x2,y2)
                    except ValueError:
                        easygui.msgbox("X and Y not be empty", title="ERROR")
                if event.ui_element == bt_clear:
                    clear_screen()
        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(surface)
    pygame.display.update()
    
